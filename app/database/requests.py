from app.database.models import async_session
from app.database.models import User, Review

from sqlalchemy import select
from sqlalchemy.sql import func


async def set_user(tg_id):
	async with async_session() as session:
		user = await session.scalar(select(User).where(User.tg_id == tg_id))

		if not user:
			session.add(User(tg_id = tg_id))
			await session.commit()


async def set_user_review(tg_id, review, mark):
	async with async_session() as session:
		user_review = await session.scalar(select(Review).where(Review.tg_id == tg_id))

		if not user_review:
			session.add(Review(tg_id = tg_id, review = review, mark = mark))
			await session.commit()


async def get_review(user_id):
	async with async_session() as session:
		query = select(Review).filter(Review.id == user_id)
		result = await session.execute(query)
		return result.scalar_one()


async def get_next_review(current_id):
	async with async_session() as session:
		query = select(Review.review, Review.mark).filter(Review.id > current_id).order_by(Review.id)
		result = await session.execute(query)
		return result.first()


async def get_previous_review(current_id):
	async with async_session() as session:
		query = select(Review.review, Review.mark).filter(Review.id < current_id).order_by(Review.id.desc())
		result = await session.execute(query)
		return result.first()


async def get_max_review_id():
	async with async_session() as session:
		return await session.scalar(select(func.max(Review.id)))


class ReviewState:
	def __init__(self):
		self.user_id = 1

	async def get_review(self):
		all_info = await get_review(self.user_id)
		formatted_text = f"Отзыв: {all_info.review}\n\nОценка: {all_info.mark}/5"
		return formatted_text
