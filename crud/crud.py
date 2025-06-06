from handler.log_handler import log_handler
from models import Tea
from fastapi import HTTPException
from handler.config import logger
from db import database
from models.FactoryStocks import FactoryStocks
from models.Response import GenericResponse
from models.Tea import Tea
import uuid
import csv


class Crud:
    def __init__(self):
        self.db_calls = database.Database()

    @log_handler
    def add_tea_in_bulk(self,contents):
        try:
            decoded = contents.decode('utf-8').splitlines()
            reader = csv.DictReader(decoded)
            teas = []

            for row in reader:
                tea = Tea(
                    id=str(uuid.uuid4()) if not row.get("id") else row["id"],
                    name=row["name"],
                    origin=row["origin"],
                    price=int(row["price"])
                )
                self.add_new_tea(tea)
                teas.append(tea)

            return {"message": f"{len(teas)} teas uploaded successfully."}

        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Error processing file: {str(e)}")
    @log_handler
    def add_new_tea(self, tea: Tea) -> GenericResponse:
        try:
            connection = self.db_calls.create_connection()
            cursor = connection.cursor()
            if tea.id:
                try:
                    tea_uuid = uuid.UUID(str(tea.id))  # Validate UUID format
                except (ValueError, AttributeError) as e:
                    logger.error("Expecting tea_id to be in uuid format", e)
                    tea_uuid = str(uuid.uuid4())

                cursor.execute("SELECT 1 FROM TEA_HUB WHERE id = ?", (str(tea_uuid),))
                exists = cursor.fetchone()
                if exists:
                    tea_id = str(tea_uuid)
                else:
                    tea_id = str(uuid.uuid4())
            else:
                tea_id = str(uuid.uuid4())

            cursor.execute(
                "INSERT INTO TEA_HUB (id, name, origin, price) VALUES (?, ?, ?, ?)",
                (str(tea_id), tea.name, tea.origin, tea.price)
            )
            connection.commit()
            connection.close()
            return GenericResponse(success=True, data={"message": f"{tea} added successfully.", "id": tea_id})
        except Exception as e:
            return GenericResponse(success=False, error=str(e))

    @log_handler
    def remove_tea(self, tea_id: int) -> GenericResponse:
        try:
            connection = self.db_calls.create_connection()
            cursor = connection.cursor()
            cursor.execute("DELETE FROM TEA_HUB WHERE id = ?", (tea_id,))
            connection.commit()
            connection.close()
            return GenericResponse(success=True, data={"message": f"Tea with id {tea_id} removed."})
        except Exception as e:
            return GenericResponse(success=False, error=str(e))

    @log_handler
    def get_all_tea(self) -> GenericResponse:
        try:
            connection = self.db_calls.create_connection()
            cursor = connection.cursor()
            cursor.execute("SELECT id, name, origin, price FROM TEA_HUB")
            rows = cursor.fetchall()
            connection.close()
            teas = [Tea(id=row[0], name=row[1], origin=row[2], price=row[3]) for row in rows]
            return GenericResponse(success=True, data={"teas": teas})
        except Exception as e:
            logger.error(f"Error occurred while fetching tea records: {str(e)}", exc_info=True)
            return GenericResponse(success=False, error=str(e))

    @log_handler
    def get_tea_from_id(self, tea_id: uuid.UUID) -> GenericResponse:
        try:
            connection = self.db_calls.create_connection()
            cursor = connection.cursor()
            cursor.execute("SELECT id, name, origin, price FROM TEA_HUB WHERE id = ?", (tea_id,))
            row = cursor.fetchone()
            connection.close()
            if row:
                tea = Tea(id=row[0], name=row[1], origin=row[2], price=row[3])
                return GenericResponse(success=True, data={"tea": tea})
            return GenericResponse(success=False, error=f"No Tea found with id: {tea_id}")
        except Exception as e:
            return GenericResponse(success=False, error=str(e))

    @log_handler
    def update_tea(self, tea: Tea) -> GenericResponse:
        try:
            connection = self.db_calls.create_connection()
            cursor = connection.cursor()

            # Check if tea exists before updating
            cursor.execute("SELECT id FROM TEA_HUB WHERE id = ?", (tea.id,))
            if cursor.fetchone() is None:
                connection.close()
                return GenericResponse(success=False, error=f"No Tea found with id: {tea.id}")

            cursor.execute(
                "UPDATE TEA_HUB SET name = ?, origin = ?, price = ? WHERE id = ?",
                (tea.name, tea.origin, tea.price, tea.id)
            )
            connection.commit()
            connection.close()
            return GenericResponse(success=True, data={"message": f"Tea with id {tea.id} updated successfully."})
        except Exception as e:
            return GenericResponse(success=False, error=str(e))

    def tea_validation(self, tea: Tea):
        value = self.get_tea_from_id(tea.id)
        if value.success:
            logger.info("Found tea in databse")
            return True
        return False

    @log_handler
    def add_factory_details(self, factory: FactoryStocks):
        try:
            factory_id = uuid.uuid4()
            connection = self.db_calls.create_connection()
            cursor = connection.cursor()
            if self.tea_validation(factory.tea_details):
                cursor.execute(
                    "INSERT INTO FACTORY_HUB (factory_id,factory_name, tea_id, quantity, price) VALUES (?, ?, ?, ?,?)",
                    (str(factory_id), factory.factory_name, factory.tea_details.id, factory.quantity, factory.price)
                )
                connection.commit()
                connection.close()

                return GenericResponse(success=True,
                                       data={"message": f"{factory} added successfully.", "factory_id": factory_id})
            else:
                return GenericResponse(success=False,
                                       data={"errorMessage": "Tea should be listed before adding factory details"})
        except Exception as e:
            return GenericResponse(success=False, error=str(e))

    def get_all_factory(self):
        try:
            connection = self.db_calls.create_connection()
            cursor = connection.cursor()
            cursor.execute("SELECT  factory_id,factory_name, tea_id, quantity, price FROM FACTORY_HUB")
            rows = cursor.fetchall()
            connection.close()
            factory = []
            for row in rows:
                val: Tea = self.get_tea_from_id(row[2]).data
                value = val.get('tea')
                tea = Tea(id=value.id, name=value.name, origin=value.origin, price=value.price)
                logger.info(f"got {tea}")
                factory.append(
                    FactoryStocks(factory_id=row[0], factory_name=row[1],
                                  tea_details=tea, quantity=row[3],
                                  price=row[4]
                                  ))

            return GenericResponse(success=True, data={"teas": factory})
        except Exception as e:
            return GenericResponse(success=False, error=str(e))
