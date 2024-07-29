from fastapi import FastAPI
from testcaseRequestContext import testcaseRequestContext

app = FastAPI()

@app.post("/testcase/")
async def posttestcase(context: testcaseRequestContext):
   return {"testcase":{"case1":"testcase1", "case2":"testcase2"}, "testscript":{"case1":"testcase1", "case2":"testcase2"}}

@app.get("/testcase/{testcase_id}")
async def gettestcase(testcase_id: str):
   return {"testcase_id": testcase_id};

@app.put("/testcase/{testcase_id}")
async def puttestcase(testcase_id: str):
   return {"testcase_id": testcase_id};

@app.delete("/testcase/{testcase_id}")
async def deletetestcase(testcase_id: str):
   return {"testcase_id": testcase_id};