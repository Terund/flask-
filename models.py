from main import models


class BaseModel(models.Model):
    __abstract__ = True  # 声明当前类是抽象类，被继承调用不被创建
    id = models.Column(models.Integer, primary_key=True, autoincrement=True)

    def save(self):
        db = models.session()
        db.add(self)
        db.commit()

    def delete(self):
        db = models.session()
        db.delete(self)
        db.commit()


class ArticleType(BaseModel):
    __tablename__ = "articletype"
    id = models.Column(models.Integer, primary_key=True)
    type = models.Column(models.String(32))
