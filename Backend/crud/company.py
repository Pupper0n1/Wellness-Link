from sqlalchemy import select, delete, orm
from sqlalchemy.ext.asyncio import AsyncSession
from litestar.exceptions import HTTPException
from uuid import UUID

from models.company import Company
from schemas.company import CompanySchema
from models.medicine import Medicine

async def get_company_list(session: AsyncSession, limit, offset) -> list[Company]:
    query = select(Company).options(orm.selectinload(Company.medicines)).limit(limit).offset(offset)
    result = await session.execute(query)
    return result.scalars().all()


async def get_company_by_name(session: AsyncSession, name: str) -> Company:
    query = select(Company).options(orm.selectinload(Company.medicines)).where(Company.name == name)
    result = await session.execute(query)
    return result.scalar_one_or_none()


async def get_company_by_id(session: AsyncSession, id: UUID) -> Company:
    query = select(Company).options(orm.selectinload(Company.medicines)).where(Company.id == id)
    result = await session.execute(query)
    return result.scalar_one_or_none()