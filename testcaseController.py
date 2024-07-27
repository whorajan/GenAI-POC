from fastapi import FastAPI
from testcaseRequestContext import testcaseRequestContext

app = FastAPI()

@app.post("/testcase/")
async def posttestcase(context: testcaseRequestContext):
   return {"testcase":{"case1":"testcase1", "case2":"testcase2"}, "testscript":{"case1":"testcase1", "case2":"testcase2"}}