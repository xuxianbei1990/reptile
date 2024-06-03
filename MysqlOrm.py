
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker

# 创建数据库连接引擎
# 这里假设你的MySQL服务器运行在localhost，用户名是'root'，密码是'password'，数据库名是'mydatabase'
engine = create_engine('mysql+mysqlconnector://root:pinyiche8888@129.211.3.200/pinyiche_pro')

# 创建基础模型类
Base = declarative_base()


    # 创建表（如果它们还不存在）
Base.metadata.create_all(engine)

# 创建会话类
Session = sessionmaker(bind=engine)

# 创建一个会话实例
session = Session()

# 添加一个新用户
new_user = User(name='newuser', fullname='New User', nickname='newnick')
session.add(new_user)
session.commit()

# 查询所有用户
users = session.query(User).all()
for user in users:
    print(user)

# 更新用户
user_to_update = session.query(User).filter_by(name='newuser').first()
user_to_update.name = 'updateduser'
user_to_update.fullname = 'Updated User'
session.commit()

# 删除用户
user_to_delete = session.query(User).filter_by(name='updateduser').first()
session.delete(user_to_delete)
session.commit()

# 关闭会话
session.close()


