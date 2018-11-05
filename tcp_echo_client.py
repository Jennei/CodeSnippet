#!usr/bin/env python  
#-*- coding:utf-8 -*-

""" 
@author:    nico 
@file:      tcp_echo_client.py 
@time:      2018/09/27 
""" 

import asyncio


async def tcp_echo_client(msg):
    reader, writer = await asyncio.open_connection(host='localhost', port=8001)
    print(f'Send:{msg!r}')
    writer.write(msg.encode())
    data = await reader.read(100)
    print(f'Received:{data.decode()!r}')
    print('Close the connection')
    writer.close()

if __name__ == '__main__':
    asyncio.run(tcp_echo_client('this is client !'))