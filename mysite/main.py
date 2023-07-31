from fastapi import FastAPI

import tools

app = FastAPI()


@app.get("/cpu_times")
def get_cpu_times_info():
    return tools.get_cpu_times()

@app.get("/cpu_count")
def get_cpu_count():
    return tools.get_cpu_count()

@app.get("/getloadavg")
def get_getloadavg():
    return tools.get_getloadavg()

@app.get("/virtual_memory")
def get_virtual_memory_info():
    return tools.get_virtual_memory()

@app.get("/swap_memory")
def get_swap_memory_info():
    return tools.get_swap_memory()