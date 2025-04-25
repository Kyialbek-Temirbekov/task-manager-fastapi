from fastapi import Depends, APIRouter
from sqlalchemy import text
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError

from ...db.database import get_db

router = APIRouter()

@router.get("/db")
async def check_db_connection(db: Session = Depends(get_db)):
    try:
        sql_query = """
        SELECT 
            current_database() AS database_name,
            current_user AS database_owner,
            current_schema() AS current_schema;
        """
        
        # Execute the query
        result = db.execute(text(sql_query))
        
        # Fetch the first row of the result
        row = result.fetchone()
        
        if row:
            # Accessing row by column name, this should work because SQLAlchemy's ResultProxy
            # returns a row object that can be accessed like a dictionary.
            return {
                "database_name": row[0],
                "database_owner": row[1],
                "current_schema": row[2]
            }
        else:
            return {"status": "failed to fetch data"}
    
    except SQLAlchemyError as e:
        return {"status": "failed to connect", "error": str(e)}