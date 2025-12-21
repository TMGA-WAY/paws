# from fastapi import APIRouter, HTTPException
# from typing import List
# from snoot.database.model import
#
# router = APIRouter()
#
# hosts_db: List[HostIdentity] = []
#
# @router.get("/", response_model=List[HostIdentity])
# def get_all_hosts():
#     return hosts_db
#
# @router.get("/{host_id}", response_model=HostIdentity)
# def get_host(host_id: str):
#     for host in hosts_db:
#         if str(host.id) == host_id:
#             return host
#     raise HTTPException(status_code=404, detail="Host not found")
#
# @router.post("/", response_model=HostIdentity)
# def create_host(host: HostIdentity):
#     hosts_db.append(host)
#     return host
