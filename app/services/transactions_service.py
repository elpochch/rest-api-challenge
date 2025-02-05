from sqlalchemy.ext.asyncio import AsyncSession
from app.api.schemas import EmployeeBatch, DepartmentBatch, JobBatch
from app.models.definitions import HiredEmployees, Departments, Jobs
from sqlalchemy.exc import SQLAlchemyError

class EmployeeService:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def create_employees(self, employees_batch: EmployeeBatch):
        failed_employees = []
        successful_inserts = 0
        for employee in employees_batch.records:
            try:
                async with self.session.begin_nested():
                    new_employee = HiredEmployees(
                        id=employee.id, 
                        name=employee.name, 
                        datetime=employee.datetime, 
                        department_id=employee.department_id, 
                        job_id=employee.job_id)
                    self.session.add(new_employee)
                    await self.session.flush()
                successful_inserts += 1
            except SQLAlchemyError as e:
                failed_employees.append({"employee":employee, "error": str(e)})

        await self.session.commit()        
        return {"message": "Employees insertion completed", 
                "inserted_rows": successful_inserts, 
                "failed_rows": len(failed_employees),
                "failed_employees": failed_employees}

class DepartmentService:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def create_departments(self, departments_batch: DepartmentBatch):
        failed_departments = []
        successful_inserts = 0
        for department in departments_batch.records:
            try:
                async with self.session.begin_nested():
                    new_department = Departments(
                        id=department.id, 
                        department=department.department
                    )
                    self.session.add(new_department)
                    await self.session.flush()
                successful_inserts += 1
            except SQLAlchemyError as e:
                failed_departments.append(department)
        await self.session.commit()
        return {"message": "Departments insertion completed",
                "inserted_rows": successful_inserts,
                "failed_rows": len(failed_departments),
                "failed_departments": failed_departments}

class JobService:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def create_jobs(self, jobs_batch: JobBatch):
        failed_jobs = []
        successful_inserts = 0
        for job in jobs_batch.records:
            try:
                async with self.session.begin_nested():
                    new_job = Jobs(**job.model_dump())
                    self.session.add(new_job)
                    await self.session.flush()
                successful_inserts += 1
            except SQLAlchemyError as e:
                failed_jobs.append(job)

        await self.session.commit()
        return {"message": "Jobs insertion completed",
                "inserted_rows": successful_inserts,
                "failed_rows": len(failed_jobs),
                "failed_jobs": failed_jobs}