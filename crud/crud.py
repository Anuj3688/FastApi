from models import Tea
from db import database
from models.Response import GenericResponse

class Crud:
    def __init__(self):
        self.db_calls = database.Database()

    def add_new_tea(self, tea: Tea) -> GenericResponse:
        try:
            connection = self.db_calls.create_connection()
            cursor = connection.cursor()
            cursor.execute(
                "INSERT INTO TEA_HUB (id, name, origin, price) VALUES (?, ?, ?, ?)",
                (tea.id, tea.name, tea.origin, tea.price)
            )
            connection.commit()
            connection.close()
            return GenericResponse(success=True, data={"message": f"{tea} added successfully."})
        except Exception as e:
            return GenericResponse(success=False, error=str(e))

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
            return GenericResponse(success=False, error=str(e))

    def get_tea_from_id(self, tea_id: int) -> GenericResponse:
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

