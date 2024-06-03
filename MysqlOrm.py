
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from OrderMain import OrderMain

# 创建数据库连接引擎
# 这里假设你的MySQL服务器运行在localhost，用户名是'root'，密码是'password'，数据库名是'mydatabase'
engine = create_engine('mysql+mysqlconnector://root:1@1.1.1.1/test_codegen')

# 创建基础模型类
Base = declarative_base()


    # 创建表（如果它们还不存在）
Base.metadata.create_all(engine)

# 创建会话类
Session = sessionmaker(bind=engine)

# 创建一个会话实例
session = Session()

# 添加一个新用户
# new_user = User(name='newuser', fullname='New User', nickname='newnick')
# session.add(new_user)
# session.commit()

# 查询所有
orders = session.query(OrderMain).all()
for order in orders:
    print(order)

# 更新
order_to_update = session.query(OrderMain).filter_by(order_no='DD2024042713493666766856127360064').first()
order_to_update.spu_id = '1'
order_to_update.category_id = '2'
session.commit()

# 删除
user_to_delete = session.query(OrderMain).filter_by(order_no='DD2024042713493666766856127360064').first()
session.delete(user_to_delete)
session.commit()

# 关闭会话
session.close()


