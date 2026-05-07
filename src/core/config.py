#define o banco de dados
class Config:
    SQLALCHEMY_DATABASE_URI = 'sqlite:///pfi.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False