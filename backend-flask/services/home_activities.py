from datetime import datetime, timedelta, timezone
from opentelemetry import trace
from lib.db import pool, query_wrap_array

tracer = trace.get_tracer("home.activities")

class HomeActivities:
 # def run(Logger):
 def run(cognito_user_id=None):
  #  Logger.info("home-activities")
    with tracer.start_as_current_span("home-activites-mock-data"):
      span = trace.get_current_span()
      now = datetime.now(timezone.utc).astimezone()
      span.set_attribute("app.now", now.isoformat())
 
 

      sql = query_wrap_array("""
      SELECT * from public.activities
      """)
      print(sql)
      with pool.connection() as conn:
        with conn.cursor() as cur:
          cur.execute(sql)
          # this will return a tuple
          # the first field being the data
          json = cur.fetchall()
          print("-2---------")
          for jsonn in json:
              print(jsonn)

      #return json[0]

      # if cognito_user_id != None:
      #   extra_crud = {
      #     'uuid': '248959df-3079-4947-b847-9e0892d1bab4fd',
      #     'handle':  'Lore',
      #     'message': 'My dear brother, it the humans that are the problem',
      #     'created_at': (now - timedelta(hours=1)).isoformat(),
      #     'expires_at': (now + timedelta(hours=12)).isoformat(),
      #     'likes': 1042,
      #     'replies': []
      #   }
      #   results.insert(0,extra_crud)
      # handle = results[0]['handle']
      # span.set_attribute("app.user_id", handle)
      # span.set_attribute("app.result_length", len(results))
      # return results
