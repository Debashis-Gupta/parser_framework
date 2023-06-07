import time
import pandas as pd
import numpy as np
import os
import os.path as osp
import csv
import re
import logging as logger
from helper.getting_list import get_list
logger.basicConfig(level=logger.DEBUG,format=
                   "%(asctime)s - %(levelname)s - %(message)s"
                   )
logger.info("Hare Krishna")

def show(str):
    logger.info(str)
    # print(str + ' '+time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time())))

if __name__ == "__main__":
    
    srcId_list, srcType_list, dstID_list, edgeType_list, timestamp_list=get_list()
    show("Exiting out")
    exit()
    # show("Creating Dataframe")
    # dataset = pd.DataFrame({
    #     'SrcID':srcId_list,
    #     'SrcType':srcType_list,
    #     'DstID':dstID_list,
    #     'EdgeType':edgeType_list,
    #     'Timestamp':timestamp_list
    # })
    
    # # print(dataset.head(20))
    # show("Creating Excel File")
    # dataset[:104857].to_excel("..\code\\ta1-theia-e3-official-3_d.xlsx",index=False)
    # show("Excel File Created")
    





        
