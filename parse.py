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
    # path_list = [r"data\\ta1-theia-e3-official-3.json"]
    # path_list= os.path.join("data\\","ta1-theia-e3-official-3.json")
    # print(f"Path: {path_list}")
    # # exit()
    # pattern_uuid = re.compile(r'uuid\":\"(.*?)\"') 
    # pattern_src = re.compile(r'subject\":{\"com.bbn.tc.schema.avro.cdm18.UUID\":\"(.*?)\"}')
    # pattern_dst1 = re.compile(r'predicateObject\":{\"com.bbn.tc.schema.avro.cdm18.UUID\":\"(.*?)\"}')
    # pattern_dst2 = re.compile(r'predicateObject2\":{\"com.bbn.tc.schema.avro.cdm18.UUID\":\"(.*?)\"}')
    # pattern_type = re.compile(r'type\":\"(.*?)\"')
    # pattern_time = re.compile(r'timestampNanos\":(.*?),')

    # notice_sum=1000000
    
    # srcId_list=list()
    # srcType_list=list()
    # dstID_list=list()
    # edgeType_list=list()
    # timestamp_list=list()
    # id_nodetype_map = {}
    # print("----"*5+"FIRST LOOP"+"----"*5)
    # for i in range(1):
    #     # now_path = path + '.' +str(i)
    #     # if(i>1):
    #     #     print("i is greater than 1")
    #     #     break
    #     if i==0:
    #         now_path = path_list
    #     if not osp.exists(now_path):
    #         show(f"Inside first loop : {now_path} Path not found")
    #     print(f"Now path is : {now_path}")
    #     f = open(now_path,'r',encoding="utf8")
    #     show(f"Inside - {now_path} is openning ")
    #     cnt = 0
    #     for line in f:
    #         cnt+=1
    #         if (cnt%notice_sum==0):
    #             print(f"CNT: {cnt}")
    #         if 'com.bbn.tc.schema.avro.cdm18.Event' in line or 'com.bbn.tc.schema.avro.cdm18.Host' in line: continue
    #         if 'com.bbn.tc.schema.avro.cdm18.TimeMarker' in line or 'com.bbn.tc.schema.avro.cdm18.StartMarker' in line: continue
    #         if 'com.bbn.tc.schema.avro.cdm18.UnitDependency' in line or 'com.bbn.tc.schema.avro.cdm18.EndMarker' in line: continue
    #         if len(pattern_uuid.findall(line)) == 0: print (line)
    #         uuid = pattern_uuid.findall(line)[0]
    #         subject_type = pattern_type.findall(line)

    #         if len(subject_type)<1:
    #             if 'com.bbn.tc.schema.avro.cdm18.MemoryObject' in line:
    #                 id_nodetype_map[uuid] = 'MemoryObject'
    #                 continue
    #             if 'com.bbn.tc.schema.avro.cdm18.NetFlowObject' in line:
    #                 id_nodetype_map[uuid] = 'NetFlowObject'
    #                 continue
    #             if 'com.bbn.tc.schema.avro.cdm18.UnnamedPipeObject' in line:
    #                 id_nodetype_map[uuid] = 'UnnamedPipeObject'
    #                 continue
    #         id_nodetype_map[uuid] = subject_type[0]
    # not_in_cnt =0
    # print("----"*8+"SECOND LOOP"+"----"*8)
    # for i in range(1):
    #     # now_path = path +'.'+str(i)
    #     if i==0: now_path=path_list
    #     if not osp.exists(now_path):
    #         show(f"In Second Loop : {now_path} not found")    
    #         break
    #     f = open(now_path,'r',encoding="utf8")
    #     fw = open(now_path+'_2.txt','w',encoding="utf8")
    #     cnt =0
    #     for line in f:
    #         cnt +=1
    #         if cnt % notice_sum ==0:
    #             print(f"Second Part -- CNT: {cnt}")
            
    #         if 'com.bbn.tc.schema.avro.cdm18.Event' in line:
    #             pattern = re.compile(r'subject\":{\"com.bbn.tc.schema.avro.cdm18.UUID\":\"(.*?)\"}')
    #             edgeType = pattern_type.findall(line)[0]
    #             timestamp = pattern_time.findall(line)[0]
    #             srcId = pattern_src.findall(line)
    #             if len(srcId) == 0: continue
    #             srcId = srcId[0]
    #             if not srcId in id_nodetype_map.keys(): 
    #                 not_in_cnt += 1
    #                 continue
    #             srcType = id_nodetype_map[srcId]
    #             dstId1 = pattern_dst1.findall(line)
    #             if len(dstId1) > 0  and dstId1[0] != 'null':
    #                 dstId1 = dstId1[0]
    #                 if not dstId1 in id_nodetype_map.keys():
    #                     not_in_cnt += 1
    #                     continue
    #                 dstType1 = id_nodetype_map[dstId1]
    #                 this_edge1 = str(srcId) + '\t' + str(srcType) + '\t' + str(dstId1) + '\t' + str(dstType1) + '\t' + str(edgeType) + '\t' + str(timestamp) + '\n'
    #                 srcId_list.append(srcId)
    #                 srcType_list.append(srcType)
    #                 dstID_list.append(dstId1)
    #                 edgeType_list.append(edgeType)
    #                 timestamp_list.append(timestamp)
    #                 fw.write(this_edge1)
    #         dstId2 = pattern_dst2.findall(line)
    #         if len(dstId2) > 0  and dstId2[0] != 'null':
    #             dstId2 = dstId2[0]
    #             if not dstId2 in id_nodetype_map.keys():
    #                 not_in_cnt += 1
    #                 continue
    #             dstType2 = id_nodetype_map[dstId2]
    #             this_edge2 = str(srcId) + '\t' + str(srcType) + '\t' + str(dstId2) + '\t' + str(dstType2) + '\t' + str(edgeType) + '\t' + str(timestamp) + '\n'
    #             srcId_list.append(srcId)
    #             srcType_list.append(srcType)
    #             dstID_list.append(dstId2)
    #             edgeType_list.append(edgeType)
    #             timestamp_list.append(timestamp)
    #             fw.write(this_edge2)	
            
                
    #     fw.close()
    #     f.close()
    # print(f"id_nodetype_map length: {len(id_nodetype_map)}")
    # print(f"Length of srcId : {len(srcId_list)}")
    # print(f"Length of srcType : {len(srcType_list)}")
    # print(f"Length of dstId : {len(dstID_list)}")
    # print(f"Length of edgeType : {len(edgeType_list)}")
    # print(f"Length of timestamp : {len(timestamp_list)}")
    srcId_list, srcType_list, dstID_list, edgeType_list, timestamp_list=get_list()
    show("Exiting out")
    exit()
    show("Creating Dataframe")
    dataset = pd.DataFrame({
        'SrcID':srcId_list,
        'SrcType':srcType_list,
        'DstID':dstID_list,
        'EdgeType':edgeType_list,
        'Timestamp':timestamp_list
    })
    
    # print(dataset.head(20))
    show("Creating Excel File")
    dataset[:104857].to_excel("ta1-theia-e3-official-3_d.xlsx",index=False)
    show("Excel File Created")
    





        
