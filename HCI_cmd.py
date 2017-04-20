#-*- utf-8 -*-

# HCI command     // OGF == 0x01
HCI_Command_1 ={
    0x0001, 'HCI_Inquiry', # LAP(3 octets) + inquirylength(1 octets) + num_response(1 octets)
    0x0002, 'HCI_Inquiry_Cancel', # stop inquiry ---- return status --0 is success other value is fail
    0x0003, "HCI_PerInq_Mode", # maxper_leg min_per_leg, LAP, inquiry length, num_response  return status 
    0x0004, "HCI_Exit_PerInq_Mode",# return status 
    0x0005, "HCI_Create_Conn", # bd_addr, packet_type, pageScanreptiton_mode, clock_offset, allowroleswitch
    0x0006, "HCI_Disconn", #conn_handle + reason
    0x0008, "HCI_CreConnCancel", # bd_addr  return status + bd_addr
    0x0009, "HCI_AcceptConnRequest", # bd_addr + role
    0x000a, "HCI_RejectConnReq", #bd_addr + reason
    0x000b, "HCI_LinkKeyReqReply", # bd_addr + link_key   return status+ bd_addr
    0x000c, "HCI_Lin_KeyReqNegative_Reply", # bd_addr  --- return status+bd_Addr
    0x000d, "HCI_PINCodeReqReply",
    0x000e, "HCI_PINCodeReqNegativeReply",
    0x000f, "HCI_ChangeConnectionPacketType",
    0x0011, "HCI_AuthenticationRequested",
    0x0013, "HCI_SetConnectionEncryption",
    0x0015, "HCI_ChangeConnectionLinkKey",
    0x0017, "HCI_Master_Link_Key",
    0x0019, "HCI_RemoteNameRequest",
    0x001a, "HCI_RemoteNameRequestCancel",
    0x001c, "HCI_ReadRemoteExtendedFeatures",
    0x001d, "HCI_ReadRemoteVersionInformation",
    0x001f, "HCI_ReadClockOffset",
    0x0020, "HCI_Read_LMP_Handle",
    0x0028, "HCI_SetupSynchronousConnection",
    0x0029, "HCI_AcceptSynchronousConnectionRequest",
    0x002a, "HCI_RejectSynchronousConnectionRequest",
    0x002b, "HCI_IOCapabilityRequestReply",
    0x002c, "HCI_UserConfirmationRequestReply",
    0x002d, "HCI_UserConfirmationRequestNegativeReply",
    0x002e, "HCI_UserPasskeyRequestReply",
    0x002f, "HCI_UserPasskeyRequestNegativeReply",
    0x0030, "HCI_RemoteOOBDataRequestReply",
    0x0033, "HCI_RemoteOOBDataRequestNegativeReply",
    0x0034, "HCI_IOCapabilityRequestNegativeReply",
    0x0035, "HCI_CreatePhysicalLink",
    0x0036, "HCI_Accept_Physical_Link",
    0x0037, "HCI_Disconnect_Physical_Link",
    0x0038, "HCI_Create_Logical_Link",
    0x0039, "HCI_Accept_Logical_Link",
    0x003a, "HCI_Disconnect_Logical_Link",
    0x003b, "HCI_Logical_Link_Cancel",
    0x003c, "HCI_Flow_Spec_Modify",
    0x003d, "HCI_Enhanced_Setup_Synchronous_Connection",
    0x003e, "HCI_Enhanced_Accept_Synchronous_Connection_Request",
    0x003f, "HCI_Truncated_Page",
    0x0040, "HCI_Truncated_Page_Cancel",
    0x0041, "HCI_Set_connevtion_slave_broadcast",
    0x0042, "HCI_set_connection_slave_broadcast_receive",
    0x0043, "HCI_start_synchronization_train",
    0x0044, "HCI_receive_synchronization_train",
    0x0045, "HCI_remote_OBB_extended_data_request_reply",
    }
# ogf = 0x02

HCI_Command_2 = {
    0x0001, "HCI_Hold_Mode",
    0x0002, "HCI_sniff_mode",
    0x0003, "exit_sniff_mode",
    0x0004, "HCI_park_state",
    0x0005, "HCI_exit_park_state",
    0x0006, "HCI_Qos_Stepup",
    0x0009, "HCI_Role_Discovery",
    0x000b, "HCI_Switch_role",
    0x000c, "Connection_Handle",
    0x000d, "HCI_Write_Link_policy_setting",
    0x000e, "HCI_read_Default_link_Policy_setting",
    0x000f, "HCI_Write_Defaule_Link_Policy_setting",
    0x0010, "HCI_Flow_specification",
    0x0011, "HCI_sniff_subrating",
        }

# ogf = 0x03

HCI_Comand_3 ={
        0x0001, "HCI_set_Event_mask",
        0x0003, "HCI_Reset",
        0x0005, "HCI_setEvent_Filter",
        0x0008, "HCI_Flush",
        0x0009, "HCI_readPINType",
        0x000a, "HCI_writePINType",
        0x000b, "HCI_Create_newUnit_key",
        0x000d, "HCI_Read_StoredLinkKey",
        0x0011, "HCI_Write_StoredLinkKey",
        0x0012, "HCI_DeleteStoredLinkKey",
        0x0013, "HCI_WroteLocalName",
        0x0014, "HCI_ReadLocalName",
        0x0015, "HCI_ReadConnAcceptTimeout",
        0x0016, "HCI_Write_connAccpetTimeout",
        0x0017, "HCI_ReadPageTimeOut",
        0x0018, "HCI_WritePageTimeout",
        0x0019, "HCI_ReadScanEnable",
        0x001a, "HCI_WriteScanEnable",
        0x001b, "HCI_ReadPageScanActivity",
        0x001c, "HCI_Write_pageScanActivity",
        0x001d, "HCI_Read_InquiryScanActivity",
        0x001e, "HCI_Write_InquiryScanActivity",
        0x001f, "HCI_Read_Authentication_Enable",
        0x0020, "HCI_Write_Authentication_enable",
        0x0023, "HCI_ReadClassOfDevice",
        0x0024, "HCI_WriteClassOfDevice",
        0x0025, "HCI_ReadVoiceSetting",
        0x0026, "HCI_WriteVoiceSetting",
        0x0027, "HCI_ReadAutomaticFlush_Timeout",
        0x0028, "HCI_WriteAutomaticFlush_Timeout",
        0x0029, "HCI_ReadNumBroadcast_Retransmissions",
        0x002a, "HCI_WriteNumBroadcast_Retransmissions",
        0x002b, "HCI_ReadHoldMode_Activity",
        0x002c, "HCI_WriteHoldMode_Activity",
        0x002d, "HCI_ReadTransmit_PowerLevel",
        0x002e, "HCI_ReadSynchronousFlowControl_Enable",
        0x002f, "HCI_WriteSynchronousFlowControl_Enable",
        0x0031, "HCI_SetContrlToHostFlowControl",
        0x0032, "HCI_HOSTBuffer_Size",
        0x0035, "HCI_HOSTNumberOfCompeleted_Packets",
        0x0036, "HCI_ReadLinkSupervision_Timeout",
        0x0037, "HCI_WriteLinkSupervision_Timerout",
        0x0038, "HCI_ReadNumberOfSupported_IAC",
        0x0039, "HCI_ReadCurrentIAC_LAP",
        0x003a, "HCI_WriteCurrentIAC_LAP",
        0x003f, "HCI_AFH_Host_Channel_Classification",
        0x0042, "HCI_Read_InquiryScan_Type",
        0x0043, "HCI_WriteInquiryScan_Type",
        0x0044, "HCI_ReadInquiry_Mode",
        0x0045, "HCI_WriteInquiry_mode",
        0x0046, "HCI_ReadPageScan_Type",
        0x0047, "HCI_WritePageScan_Type",
        0x0048, "HCI_AFH_ChannelAssessment_Mode",
        0x0049, "HCI_AFH_ChannelAssessment_Mode",
        0x0051, "HCI_ReadExtendedInquiry_Response",
        0x0052, "HCI_WriteExtendInquiry_Response",
        0x0053, "HCI_Refresh_Encrypption_key",
        0x0055, "HCI_ReadSimpleParing_Mode",
        0x0056, "HCI_WriteSimpleParing_Mode",
        0x0057, "HCI_Read_LocalOOB_Data",
        0x0058, "HCI_Read_InquiryResponseTransmitPowerLevel",
        0x0059, "HCI_Write_InquiryTransmitPowerLevel",
        0x0060, "HCI_SendKeyPressNotification",
        0x005a, "HCI_Read_DefaultErroneousDataReporting",
        0x005b, "HCI_Write_DefauleError_DataReporting",
        0x005f, "HCI_Enhanced_Flush",
        0x0061, "HCI_Read_LogicLinkAccept_timeout",
        0x0062, "HCI_Write_LogicLinkAccept_Timeout",
        0x0063, "HCI_SetEventMask_Page2",
        0x0064, "HCI_ReadLocation_data",
        0x0065, "HCI_WriteLocation_Data",
        0x0066, "HCO_FlowControl_Mode",
        0x0067, "HCI_WriteFlowControl_Mode",
        0x0068, "HCI_ReadEnhanceTransmitPower_Level",
        0x0069, "HCI_ReadBestEffortFlush_Timeout",
        0x006a, "HCI_WriteBestEffortFlush_Timeout",
        0x006b, "HCI_ShortRange_Mode",
        0x006c, "HCI_ReadLE_Host_Support",
        0x006d, "HCI_WriteLE_HostSupport",
        0x006e, "HCI_SetMWS_ChannelParmeters",
        0x006f, "HCI_SetExternalFrame_Conf",
        0x0070, "HCI_SetMWS_Singnaling",
        0x0071, "HCI_SetMWS_Transport_Layer",
        0x0072, "HCI_SetMWS_ScanFrequency_Table",
        0x0073, "HCI_SetMWS_PATTERNConfiguartion",
        0x0074, "HCI_SetReservedLT_Addr",
        0x0075, "HCI_DeletedReservedLT_addr",
        0x0076, "HCI_SetConnSlaveBroadcast_Data",
        0x0077, "HCI_ReadSynchronization_TrainParameters",
        0x0078, "HCI_WriteSynchronization_TrainParameters",
        0x0079, "HCI_ReadSecureConnection_HostSupport",
        0x007a, "HCI_WriteSecure_ConnectionHostSupport",
        0x007b, "HCI_ReadAuthrnticated_PayloadTimerout",
        0x007c, "HCI_WriteAuthenticated_PayloadYimeout",
        0x007d, "HCI_REadLocalOOBExtended_Data",
        0x007e, "HCI_ReadExtendedPage_Timeout",
        0x007f, "HCI_WriteExtenddPage_Timeout",
        0x0080, "HCI_ReadExtended_InquiryLength",
        0x0081, "HCI_WriteExtend_InquiryLength",
        
        }

# OGF == 0x04 
HCI_cmd_4 = {
        0x0001, "HCI_ReadLocalVersion_Information",
        0x0002, "HCI_ReadLocalSupportCommand",
        0x0003, "HCI_ReadLocalSupportFeatures",
        0x0004, "HCI_REadLocalExtendedFeatures",
        0x0005, "HCI_ReadBuffer_Size",
        0x0006, "HCI_ReadBD_addr",
        0x0007, "HCI_ReadDataBlock_Size",
        0x0008, "HCI_REadLocalSupport_Codecs",
        }


# OGF == 0x05 

HCI_cmd_5 = {
        0x0001, "HCI_ReadFailedContact_Countter",
        0x0002, "HCI_ResetFailedContact_Counter",
        0x0003, "HCI_REadLinkQuality",
        0x0005, "HCI_ReadRSSI",
        0x0006, "HCI_ReadAFHChannel_Map",
        0x0007, "HCI_ReadClock",
        0x0008, "HCI_ReadEncryptionKeySize",
        0x0009, "HCI_ReadLocalAMP_info",
        0x000a, "HCI_ReadLocalAMP_ASSOC",
        0x000b, "HCI_WriteRemoteAMP_ASSOC",
        0x000c, "HCI_GetMWSTransportLayer_Configuration",
        0x000d, "HCI_SetTriggeredClock_Capture",
        }


# HCI_Event

HCI_Event ={
        0x01, "Inquiry Compelete",
        0x02, "Inquiry Result",
        0x03, "Connection Complete",
        0x04, "connection Request",
        0x05, "Disconnection complete",
        0x06, "Authentication Complete",
        0x07, "Remote Name Request Complete",
        0x08, "Encryption Change",
        0x09, "Change Connection Link Key Complete",
        0x0a, "Master Link Key Complete",
        0x0b, "Read Remote Supported Feature Complete",
        }

# ACL Data analyze
ACL_CID ={
								
	0x0000, " NULL identifiler",
	0x0001, " L2CAP Signaling channel",
	0x0002, " connectionless channel",
								}
# ACL single 
ACL_single = {
	0x01, "command reject",
	0x02, "connection request",
	0x03, "connection response",
	0x04, "configuration request",
	0x05, "configuration response",
	0x06, "disconnection request",
	0x07, "disconnection response",
	0x08, "echo request",
	0x09, "echo response",
	0x0a, "information request",
	0x0b, "information response",
	0x0c, "create channel request",
	0x0d, "create channel response",
	0x0e, "move channel request",
	0x0f, "move channel response",
	0x10, "move channel confirmation",
	0x11, "move channel confirmation response",
	0x12, "connection parameter update request",
	0x13, "connection parameter update response",
	0x14, "LE credit based connection request",
	0x15, "LE credit based connection response",
	0x16, "LE Flow control credit",
}