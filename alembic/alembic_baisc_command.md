# 创建alembic环境
- alembic init alembic
- 修改alembic.ini
    > sqlalchemy.url = mysql+pymysql://root:111111@localhost/ohho
- 修改alembic/env.py
    > 
        将 target_metadata = None替换为
        import os
        import sys
        root = os.path.dirname(os.path.abspath(__file__)) + "/../"
        sys.path.append(root)
        from Test.models import BaseModel
        target_metadata = BaseModel.metadata
        
# 基本命令
- alembic revision --autogenerate -m "information" 
    + 相当于 makemigrations
    + 产生命令
- alembic upgrade head 
    + 相当于 migrate
    + 执行命令
    
    
# 基本问题
- Target database is not up to date
    - alembic upgrade head
    - 如果上面语句出错，把head中的upgrade和downgrade全部换成pass，再次执行上面语句