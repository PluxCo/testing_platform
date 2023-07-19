import enum

from sqlalchemy import Column, Integer, String, ForeignKey, Boolean, Text, DateTime, Enum, Table
from sqlalchemy.orm import relationship

from .db_session import SqlAlchemyBase
from .users import PersonGroup, Person


class AnswerState(enum.Enum):
    NOT_ANSWERED = 0
    TRANSFERRED = 1
    ANSWERED = 2


class QuestionGroupAssociation(SqlAlchemyBase):
    __tablename__ = "question_to_group"

    question_id = Column(ForeignKey("questions.id"), primary_key=True)
    group_id = Column(ForeignKey("person_groups.id"), primary_key=True)


class Question(SqlAlchemyBase):
    __tablename__ = "questions"

    id = Column(Integer, primary_key=True, autoincrement=True)
    text = Column(Text)
    subject = Column(String)
    options = Column(Text)
    answer = Column(Integer)
    groups = relationship("PersonGroup", secondary="question_to_group")
    level = Column(Integer)
    article_url = Column(String)


class QuestionAnswer(SqlAlchemyBase):
    __tablename__ = 'answers'

    id = Column(Integer, primary_key=True, autoincrement=True)
    question_id = Column(ForeignKey("questions.id"))
    question = relationship("Question")
    person_id = Column(ForeignKey("persons.id"))
    person = relationship("Person")
    person_answer = Column(String)
    answered_time = Column(DateTime)
    ask_time = Column(DateTime)
    state = Column(Enum(AnswerState))
