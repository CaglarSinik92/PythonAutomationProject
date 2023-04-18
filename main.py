import re
from ServisIslemleri import ServiceProcess
from DatabaseBaglantisi import OracleDB
import DriverTanimlanmasi

cross_offer_outcome = [
    [{"customer_id": "'1008417871'"}, {"channel": "Mobile"}, {"sub_channel": "6001"},
     {"functionCode": "MENUPARATRANSFER"},
     {"orgLevel": "DEPARTMENT"}, {"userRole": "RELATIONSHIP_MANAGER"}, {"outcome": "Accepted"}, {"outcome_id": "31"},
     {"suppression": 179}, {"cdm_ref_id": "Proposition 279"}, {"product_group_id": "7"},
     {"pyname": "FaturaKampanyalariChipParaOranaGore_Mobile"},
     {"test_case": "CrossOffer"}, {"suppress_offer_pyname": "FaturaKampanyalariChipParaOranaGore_Mobile"},
     {"suppress_channel": "Mobile"}, {"suppress_sub_channel": "6001"},
     {"suppress_functionCode": "MENUPARATRANSFER"}, {"suppress_cdm_ref_id": "Proposition 279"},
     {"suppress_product_group_id": "7"}],
    [{"customer_id": "'1008417871'"}, {"channel": "Mobile"}, {"sub_channel": "6001"},
     {"functionCode": "MENUPARATRANSFER"},
     {"orgLevel": "DEPARTMENT"}, {"userRole": "RELATIONSHIP_MANAGER"}, {"outcome": "Rejected"}, {"outcome_id": "32"},
     {"suppression": 179}, {"cdm_ref_id": "Proposition 279"}, {"product_group_id": "7"},
     {"pyname": "FaturaKampanyalariChipParaOranaGore_Mobile"},
     {"test_case": "CrossOffer"}, {"suppress_offer_pyname": "FaturaKampanyalariChipParaOranaGore_Mobile"},
     {"suppress_channel": "Mobile"}, {"suppress_sub_channel": "6001"},
     {"suppress_functionCode": "MENUPARATRANSFER"}, {"suppress_cdm_ref_id": "Proposition 279"},
     {"suppress_product_group_id": "7"}],
    [{"customer_id": "'1008417871'"}, {"channel": "Mobile"}, {"sub_channel": "6001"},
     {"functionCode": "MENUPARATRANSFER"},
     {"orgLevel": "DEPARTMENT"}, {"userRole": "RELATIONSHIP_MANAGER"}, {"outcome": "Ongoing"}, {"outcome_id": "33"},
     {"suppression": 179}, {"cdm_ref_id": "Proposition 279"}, {"product_group_id": "7"},
     {"pyname": "FaturaKampanyalariChipParaOranaGore_Mobile"},
     {"test_case": "CrossOffer"}, {"suppress_offer_pyname": "FaturaKampanyalariChipParaOranaGore_Mobile"},
     {"suppress_channel": "Mobile"}, {"suppress_sub_channel": "6001"},
     {"suppress_functionCode": "MENUPARATRANSFER"}, {"suppress_cdm_ref_id": "Proposition 279"},
     {"suppress_product_group_id": "7"}],
    [{"customer_id": "'1008417871'"}, {"channel": "Mobile"}, {"sub_channel": "6001"},
     {"functionCode": "MENUPARATRANSFER"},
     {"orgLevel": "DEPARTMENT"}, {"userRole": "RELATIONSHIP_MANAGER"}, {"outcome": "Indecisive"}, {"outcome_id": "34"},
     {"suppression": 179}, {"cdm_ref_id": "Proposition 279"}, {"product_group_id": "7"},
     {"pyname": "FaturaKampanyalariChipParaOranaGore_Mobile"},
     {"test_case": "CrossOffer"}, {"suppress_offer_pyname": "FaturaKampanyalariChipParaOranaGore_Mobile"},
     {"suppress_channel": "Mobile"}, {"suppress_sub_channel": "6001"},
     {"suppress_functionCode": "MENUPARATRANSFER"}, {"suppress_cdm_ref_id": "Proposition 279"},
     {"suppress_product_group_id": "7"}]]

product_offer_outcome = [
    [{"customer_id": "'1008917620'"}, {"channel": "CallCenter"}, {"sub_channel": "3013"}, {"functionCode": "FIZ"},
     {"orgLevel": "CALL_CENTRE"},
     {"userRole": "GROUPSALESMANAGER"}, {"outcome": "Accepted"}, {"outcome_id": "31"}, {"suppression": 59},
     {"cdm_ref_id": "Proposition 114"},
     {"product_group_id": "7"}, {"pyname": "TLVadesizOtomatikFaturaTalimati_InboundCC"},
     {"test_case": "ProductGroupSuppression"},
     {"suppress_offer_pyname": "TLVadesizVergiSGK_Branch"}, {"suppress_channel": "Branch"},
     {"suppress_sub_channel": "100102"}, {"suppress_functionCode": "FIZ"}, {"suppress_cdm_ref_id": "Proposition 24"},
     {"suppress_product_group_id": "7"}, {"bucket_name": "CallCenter-Phase2"},
     {"graph_name": "TLVadesizOtomatikFaturaTalimati_CC"}, {"graph_prefix": "10055"},
     {"suppress_bucket_name": "Branch-Phase1"},
     {"suppress_graph_name": "TL Vadesiz Vergi SGK"}, {"suppress_graph_prefix": "10013"},
     {"suppress_org_level": "DEPARTMENT"}, {"suppress_user_role": "RELATIONSHIP_MANAGER"}]]

service = ServiceProcess()


def context_data_definition(channel, subchannel, functionCode, orgLevel, userRole):
    if channel == "Branch":
        context_data = "requester==GetOffers;;DynamicPriceTestEnvironment==Default;;channel==" + channel + ";;subchannel==" + subchannel + ";;LogicType==Retention,CrossSell;;customerInContact==false;;fetchAll==true;;functionCode==" + functionCode + ";;FunctionDataList::SMARTLISTPRODUCTCODES==1|LOG_CALL_SOURCE==GO_FIZ;;UserContext::orgLevel==" + orgLevel + "|userRole==" + userRole + "|username==48018"
        return context_data
    if channel == "Mobile":
        context_data = "requester==GetOffers;;DynamicPriceTestEnvironment==Default;;channel==" + channel + ";;subchannel==" + subchannel + ";;LogicType==Retention,CrossSell;;customerInContact==false;;fetchAll==false;;functionCode==" + functionCode + ";;FunctionDataList::OS_NAME==IOS|APP_VERSION==042000|LOG_CALL_SOURCE==GTO"
        return context_data
    if channel == "CallCenter":
        context_data = "requester==GetOffers;;dynamicPriceTestEnvironment==Default;;channel==" + channel + ";;subchannel==" + subchannel + ";;LogicType==Retention,CrossSell;;customerInContact==false;;fetchAll==true;;functionCode==" + functionCode + ";;FunctionDataList:: LOG_CALL_SOURCE==GO_FIZ_CC;;UserContext::orgLevel==" + orgLevel + "|userRole==" + userRole + "|username==48018"
        return context_data


def cross_offer_ih_check_dif_channel(cust_id, channel, subchannel, functionCode, orgLevel, userRole, outcome,
                                     outcome_id, pyname, suppression_time_temp, suppress_channel, suppress_sub_channel,
                                     suppress_functionCode, suppress_offer_pyname):
    print(f"\n************************CrossOffer IH CHECK FOR {outcome} TODAY STARTS***********************\n")
    # delete ih
    database.delete("INTERACTION_HISTORY_V", "CUSTOMERID = " + cust_id)
    # delete supplement
    database.delete("IH_SUPPLEMENT", "MUSTERIID =" + cust_id)
    database.delete("CDM_IH", "MUSTERIID = " + cust_id)
    service_cust_id = cust_id.replace("'", "")
    context_data = context_data_definition(suppress_channel, suppress_sub_channel, suppress_functionCode, orgLevel,
                                           userRole)
    print("getOffer Request and Response:")
    service.getOfferResponse(service_cust_id, context_data, suppress_offer_pyname)
    if service.is_offer_presented:
        print("\nCaptureResponse Request and Response: ")
        service.captureResp(outcome, service_cust_id, outcome_id, suppress_sub_channel, suppress_functionCode)
        print("\ngetOffer Request and Response: ")
        context_data = context_data_definition(channel, subchannel, functionCode, orgLevel,
                                               userRole)
        service.getOfferResponse(service_cust_id, context_data, pyname)
        if service.is_offer_presented:
            print("\nTest Case Failed same day offer is presented")
            database.select("IH_SUPPLEMENT", "*", "MUSTERIID = " + cust_id)
            database.select("INTERACTION_HISTORY_V", "*", "CUSTOMERID = " + cust_id)
        else:
            print(f"\nIn suppression period: {suppression_time_temp} Outcome: {outcome} Pyname : {pyname}\n")
            date_update = "OUTCOMETIME = SYSDATE-" + str(suppression_time_temp)
            print("Outcometime is updated :")
            database.update("INTERACTION_HISTORY_V", date_update, "CUSTOMERID = " + cust_id)
            service.getOfferResponse(service_cust_id, context_data, pyname)
            if service.is_offer_presented:
                print(f"\nTest Case Failed after {suppression_time_temp}")
                database.select("IH_SUPPLEMENT", "*", "MUSTERIID = " + cust_id)
                database.select("INTERACTION_HISTORY_V", "*", "CUSTOMERID = " + cust_id)
            else:
                print(f"\nIn suppression period: {suppression_time_temp + 1} Outcome: {outcome} Pyname : {pyname}\n")
                date_update = "OUTCOMETIME = SYSDATE-" + str(suppression_time_temp + 1)
                print("Outcometime is updated :")
                database.update("INTERACTION_HISTORY_V", date_update, "CUSTOMERID = " + cust_id)
                print("\ngetOffer service request and Response:")
                service.getOfferResponse(service_cust_id, context_data, pyname)
                if service.is_offer_presented:
                    print("\nDatabase Select Records: ")
                    database.select("IH_SUPPLEMENT", "*", "MUSTERIID = " + cust_id)
                    database.select("INTERACTION_HISTORY_V", "*", "CUSTOMERID = " + cust_id)
                    print(
                        f"\nTest Case Passed for Suppression Day: {suppression_time_temp + 1} and Outcome: {outcome}\n  and Pyname: {pyname}\n")
                else:
                    print(f"\nTest Case Failed after {suppression_time_temp + 1}")
                    database.select("IH_SUPPLEMENT", "*", "MUSTERIID = " + cust_id)
                    database.select("INTERACTION_HISTORY_V", "*", "CUSTOMERID = " + cust_id)
    else:
        print("offer is not presented")
        database.select("IH_SUPPLEMENT", "*", "MUSTERIID = " + cust_id)
        database.select("INTERACTION_HISTORY_V", "*", "CUSTOMERID = " + cust_id)
    database.delete("INTERACTION_HISTORY_V", "CUSTOMERID = " + cust_id)
    # delete supplement
    database.delete("IH_SUPPLEMENT", "MUSTERIID =" + cust_id)
    database.delete("CDM_IH", "MUSTERIID = " + cust_id)


def cross_offer_cdm_ih_check_dif_channel(cust_id, channel, subchannel, functionCode, orgLevel, userRole, outcome,
                                         outcome_id, pyname, suppression_time_temp, suppress_channel,
                                         suppress_sub_channel,
                                         suppress_functionCode, suppress_offer_pyname, suppress_cdm_ref_id,
                                         suppress_product_group_id):
    print(f"\n************************CrossOffer CDM-IH CHECK FOR {outcome} TODAY STARTS***********************\n")
    # delete ih
    database.delete("INTERACTION_HISTORY_V", "CUSTOMERID = " + cust_id)
    # delete supplement
    database.delete("IH_SUPPLEMENT", "MUSTERIID =" + cust_id)
    database.delete("CDM_IH", "MUSTERIID = " + cust_id)
    suppress_cdm_ref_id = "'" + suppress_cdm_ref_id + "'"
    suppress_channel = "'" + suppress_channel + "'"
    outcome = "'" + outcome + "'"
    service_cust_id = cust_id.replace("'", "")
    cdm_ih_values = service_cust_id + ", sysdate, " + suppress_cdm_ref_id + ", " + outcome + ", " + outcome_id + ", NULL, " + suppress_product_group_id + ", " + suppress_channel + ", NULL, NULL"
    print("\nCDM-IH Record: ")
    database.insert("APPS.CDM_IH",
                    "MUSTERIID, OUTCOMETIME, CDMREFID, OUTCOME, SUBRESPONSECODE, REASONCODE, PRODUCTGROUP, CHANNEL, PRESENTATIONTYPE, OPERATIONTYPE",
                    cdm_ih_values)
    print("Database record for CDM-IH: ")
    database.select("APPS.CDM_IH", "*", "MUSTERIID =" + cust_id)

    print("\ngetOffer Request and Response: ")
    context_data = context_data_definition(channel, subchannel, functionCode, orgLevel,
                                           userRole)
    # Servis çağrıldı
    service.getOfferResponse(service_cust_id, context_data, pyname)
    if service.is_offer_presented:
        # eğer teklif gelirse test case failed
        print("\nTest Case Failed today suppression")
        database.select("IH_SUPPLEMENT", "*", "MUSTERIID = " + cust_id)
        database.select("APPS.CDM_IH", "*", "MUSTERIID =" + cust_id)
    else:
        # 14 gün önceye çekildi
        print(f"\nIn suppression period: {suppression_time_temp} Outcome: {outcome}, Pyname : {pyname} \n")
        date_update = "SYSDATE-" + str(suppression_time_temp)
        print(f"Outcometime is updated : {suppression_time_temp}, for Outcome: {outcome}, Pyname : {pyname}")
        database.delete("CDM_IH", "MUSTERIID = " + cust_id)
        cdm_ih_values = service_cust_id + ", " + date_update + ", " + suppress_cdm_ref_id + ", " + outcome + ", " + outcome_id + ", NULL, " + suppress_product_group_id + ", " + suppress_channel + ", NULL, NULL"
        database.insert("APPS.CDM_IH",
                        "MUSTERIID, OUTCOMETIME, CDMREFID, OUTCOME, SUBRESPONSECODE, REASONCODE, PRODUCTGROUP, CHANNEL, PRESENTATIONTYPE, OPERATIONTYPE",
                        cdm_ih_values)
        print("Database record for CDM-IH")
        database.select("APPS.CDM_IH", "*", "MUSTERIID =" + cust_id)
        # geOffer sonucunda offer gelirse test case fail
        print("\ngetOffer service Request and Response: ")
        service.getOfferResponse(service_cust_id, context_data, pyname)
        if service.is_offer_presented:
            print(f"\nTest Case Failed at suppression period :{suppression_time_temp}")
            database.select("IH_SUPPLEMENT", "*", "MUSTERIID = " + cust_id)
            database.select("APPS.CDM_IH", "*", "MUSTERIID =" + cust_id)
        else:
            # 15 gün önceye çekilde teklif gelirse test case apssed
            print(f"\nIn suppression period: {suppression_time_temp + 1} Outcome: {outcome}, Pyname : {pyname}\n")
            date_update = "SYSDATE-" + str(suppression_time_temp + 1)
            print(f"Outcometime is updated : {suppression_time_temp + 1}")
            database.delete("CDM_IH", "MUSTERIID = " + cust_id)
            cdm_ih_values = service_cust_id + ", " + date_update + ", " + suppress_cdm_ref_id + ", " + outcome + ", " + outcome_id + ", NULL, " + suppress_product_group_id + ", " + suppress_channel + ", NULL, NULL"
            database.insert("APPS.CDM_IH",
                            "MUSTERIID, OUTCOMETIME, CDMREFID, OUTCOME, SUBRESPONSECODE, REASONCODE, PRODUCTGROUP, CHANNEL, PRESENTATIONTYPE, OPERATIONTYPE",
                            cdm_ih_values)
            database.select("APPS.CDM_IH", "*", "MUSTERIID =" + cust_id)
            print("\n")
            service.getOfferResponse(service_cust_id, context_data, pyname)
            if service.is_offer_presented:
                print("Database Records: ")
                database.select("IH_SUPPLEMENT", "*", "MUSTERIID = " + cust_id)
                database.select("APPS.CDM_IH", "*", "MUSTERIID =" + cust_id)
                print(
                    f"\nTest Case passed for suppression duration : {suppression_time_temp + 1} and for Outcome: {outcome}, Pyname : {pyname}\n")
            else:
                print(f"Test Case Failed at suppression period : {suppression_time_temp + 1}\n")
                database.select("IH_SUPPLEMENT", "*", "MUSTERIID = " + cust_id)
                database.select("APPS.CDM_IH", "*", "MUSTERIID =" + cust_id)
    database.delete("INTERACTION_HISTORY_V", "CUSTOMERID = " + cust_id)
    # delete supplement
    database.delete("IH_SUPPLEMENT", "MUSTERIID =" + cust_id)
    database.delete("CDM_IH", "MUSTERIID = " + cust_id)


def offer_self_contention_ih_check_dif_channel(cust_id, channel, subchannel, functionCode, orgLevel, userRole, outcome,
                                               outcome_id, pyname, suppression_time_temp, suppress_channel,
                                               suppress_sub_channel,
                                               suppress_functionCode, suppress_offer_pyname):
    print(f"\n************************CrossOffer IH CHECK FOR {outcome} TODAY STARTS***********************\n")

    service_cust_id = cust_id.replace("'", "")
    context_data = context_data_definition(suppress_channel, suppress_sub_channel, suppress_functionCode, orgLevel,
                                           userRole)
    print("getOffer Request and Response:")
    service.getOfferResponse(service_cust_id, context_data, suppress_offer_pyname)
    if service.is_offer_presented:
        print("\nCaptureResponse Request and Response: ")
        service.captureResp(outcome, service_cust_id, outcome_id, suppress_sub_channel, suppress_functionCode)
        print("\ngetOffer Request and Response: ")
        context_data = context_data_definition(channel, subchannel, functionCode, orgLevel,
                                               userRole)
        service.getOfferResponse(service_cust_id, context_data, pyname)
        if service.is_offer_presented:
            print("\nTest Case Failed same day offer is presented")
            database.select("IH_SUPPLEMENT", "*", "MUSTERIID = " + cust_id)
            database.select("INTERACTION_HISTORY_V", "*", "CUSTOMERID = " + cust_id)
        else:
            print(f"\nIn suppression period: {suppression_time_temp} Outcome: {outcome} Pyname : {pyname}\n")
            date_update = "OUTCOMETIME = SYSDATE-" + str(suppression_time_temp)
            print("Outcometime is updated :")
            database.update("INTERACTION_HISTORY_V", date_update, "CUSTOMERID = " + cust_id)
            service.getOfferResponse(service_cust_id, context_data, pyname)
            if service.is_offer_presented:
                print(f"\nTest Case Failed after {suppression_time_temp}")
                database.select("IH_SUPPLEMENT", "*", "MUSTERIID = " + cust_id)
                database.select("INTERACTION_HISTORY_V", "*", "CUSTOMERID = " + cust_id)
            else:
                print(f"\nIn suppression period: {suppression_time_temp + 1} Outcome: {outcome} Pyname : {pyname}\n")
                date_update = "OUTCOMETIME = SYSDATE-" + str(suppression_time_temp + 1)
                print("Outcometime is updated :")
                database.update("INTERACTION_HISTORY_V", date_update, "CUSTOMERID = " + cust_id)
                print("\ngetOffer service request and Response:")
                service.getOfferResponse(service_cust_id, context_data, pyname)
                if service.is_offer_presented:
                    print("\nDatabase Select Records: ")
                    database.select("IH_SUPPLEMENT", "*", "MUSTERIID = " + cust_id)
                    database.select("INTERACTION_HISTORY_V", "*", "CUSTOMERID = " + cust_id)
                    print(
                        f"\nTest Case Passed for Suppression Day: {suppression_time_temp + 1} and Outcome: {outcome}\n  and Pyname: {pyname}\n")
                else:
                    print(f"\nTest Case Failed after {suppression_time_temp + 1}")
                    database.select("IH_SUPPLEMENT", "*", "MUSTERIID = " + cust_id)
                    database.select("INTERACTION_HISTORY_V", "*", "CUSTOMERID = " + cust_id)
    else:
        print("offer is not presented")
        database.select("IH_SUPPLEMENT", "*", "MUSTERIID = " + cust_id)
        database.select("INTERACTION_HISTORY_V", "*", "CUSTOMERID = " + cust_id)
    database.delete("INTERACTION_HISTORY_V", "CUSTOMERID = " + cust_id)
    # delete supplement
    database.delete("IH_SUPPLEMENT", "MUSTERIID =" + cust_id)
    database.delete("CDM_IH", "MUSTERIID = " + cust_id)


def product_group_suppression_ih_check(primary_customer_id, secondary_customer, channel, subchannel, function_code,
                                       org_level, user_role, outcome, outcome_id, pyname,
                                       suppression_time,
                                       suppress_channel, suppress_sub_channel,
                                       suppress_function_code, suppress_offer_pyname, suppress_org_level_tmp,
                                       suppress_user_role_tmp):
    print(f"\n************************CrossOffer IH CHECK FOR {outcome} TODAY STARTS***********************\n")

    database.delete("INTERACTION_HISTORY_V", "CUSTOMERID = " + secondary_customer)
    database.delete("IH_SUPPLEMENT", "MUSTERIID =" + secondary_customer)
    database.delete("CDM_IH", "MUSTERIID = " + secondary_customer)

    service_cust_id = secondary_customer.replace("'", "")
    context_data = context_data_definition(suppress_channel, suppress_sub_channel, suppress_function_code,
                                           suppress_org_level_tmp,
                                           suppress_user_role_tmp)
    print("getOffer Request and Response:")
    service.getOfferResponse(service_cust_id, context_data, suppress_offer_pyname)

    print("\nDB record for IH-SUPPLEMENT: ")
    db_result = database.select("IH_SUPPLEMENT", "*", "MUSTERIID = " + secondary_customer)
    print(db_result)

    if service.is_offer_presented:
        print("\nCaptureResponse Request and Response: ")
        service.captureResp(outcome, service_cust_id, outcome_id, suppress_sub_channel, suppress_function_code)
        print(service.treatment_id)

        print("\nDB record for Some Table: ")
        db_result = database.select("PGA_TMUSTERI_V", "*", "MUSTERI_ID = " + secondary_customer)
        print(db_result)
        db_result = db_py_format_to_sql(db_result)
        print(db_result)


    else:
        print(f"\n{suppress_offer_pyname} is not presented!")
        print("Test Case Failed")


def db_py_format_to_sql(db_query):
    db_ready_to_insert = ""
    for item in db_query:
        db_ready_to_insert += str(item) + ","

    db_ready_to_insert = db_ready_to_insert[:-1]  # remove the last comma
    db_ready_to_insert = db_ready_to_insert.replace("None", "NULL")
    db_ready_to_insert = re.sub(r"datetime\.datetime\((\d{4}),\s(\d{1,2}),\s(\d{1,2}),\s(\d{1,2}),\s(\d{1,2})\)",
                                r"TIMESTAMP '\1-\2-\3 \4:\5:00.000000'", db_ready_to_insert)
    return db_ready_to_insert


def return_cust_id_from_prefix(prefix):
    prefix = "'%" + prefix + "%'"
    customer_id = database.select("PGA_TMUSTERI_V", "MUSTERI_ID",
                                  "MUSTERI_ID LIKE " + prefix + "AND TARIH >SYSDATE-1 ORDER BY MUSTERI_ID FETCH FIRST 1 ROWS ONLY")
    customer_id = str(customer_id).replace("[(", "")
    customer_id = str(customer_id).replace(",)]", "")
    return customer_id


def suppression_check():
    for b_outcome in product_offer_outcome:
        customer_id = b_outcome[0]['customer_id']
        channel_tmp = b_outcome[1]['channel']
        subchannel_tmp = b_outcome[2]['sub_channel']
        function_code_tmp = b_outcome[3]['functionCode']
        org_level_tmp = b_outcome[4]['orgLevel']
        user_role_tmp = b_outcome[5]['userRole']
        outcome_tmp = b_outcome[6]['outcome']
        outcome_id_tmp = b_outcome[7]['outcome_id']
        suppression_time_temp = b_outcome[8]['suppression']
        cdm_ref_id_tmp = b_outcome[9]['cdm_ref_id']
        product_group_id_tmp = b_outcome[10]['product_group_id']
        pyname_tmp = b_outcome[11]['pyname']
        test_case_tmp = b_outcome[12]['test_case']
        suppress_offer_pyname_tmp = b_outcome[13]['suppress_offer_pyname']
        suppress_channel_tmp = b_outcome[14]['suppress_channel']
        suppress_sub_channel_tmp = b_outcome[15]['suppress_sub_channel']
        suppress_function_code_tmp = b_outcome[16]['suppress_functionCode']
        suppress_cdm_ref_id_tmp = b_outcome[17]['suppress_cdm_ref_id']
        suppress_product_group_id_tmp = b_outcome[18]['suppress_product_group_id']
        bucket_name_tmp = str(b_outcome[19]['bucket_name'])
        graph_name_tmp = str(b_outcome[20]['graph_name'])
        prefix1_tmp = str(b_outcome[21]['graph_prefix'])
        bucket_name_sec_tmp = str(b_outcome[22]['suppress_bucket_name'])
        graph_name_sec_tmp = str(b_outcome[23]['suppress_graph_name'])
        prefix2_tmp = str(b_outcome[24]['suppress_graph_prefix'])
        suppress_org_level_tmp = str(b_outcome[25]['suppress_org_level'])
        suppress_user_role_tmp = str(b_outcome[26]['suppress_user_role'])
        if test_case_tmp == "CrossOffer":
            # IH üzerinden de kontrol edilmesi gerekebilir.
            cross_offer_ih_check_dif_channel(customer_id, channel_tmp, subchannel_tmp, function_code_tmp,
                                             org_level_tmp, user_role_tmp, outcome_tmp, outcome_id_tmp, pyname_tmp,
                                             suppression_time_temp,
                                             suppress_channel_tmp, suppress_sub_channel_tmp,
                                             suppress_function_code_tmp, suppress_offer_pyname_tmp)
            # Farklı kanal olduğu için CDM-IH üzerinden kontrol edilecek
            cross_offer_cdm_ih_check_dif_channel(customer_id, channel_tmp, subchannel_tmp, function_code_tmp,
                                                 org_level_tmp, user_role_tmp, outcome_tmp, outcome_id_tmp,
                                                 pyname_tmp,
                                                 suppression_time_temp,
                                                 suppress_channel_tmp, suppress_sub_channel_tmp,
                                                 suppress_function_code_tmp, suppress_offer_pyname_tmp,
                                                 suppress_cdm_ref_id_tmp, suppress_product_group_id_tmp)

        elif test_case_tmp == "ProductGroupSuppression":
            # Aynı product groupta olan iki farklı offer buluruz.
            driver = DriverTanimlanmasi

            # data creation
            driver.generating_data_graph(bucket_name_tmp, graph_name_tmp, bucket_name_sec_tmp, graph_name_sec_tmp)

            # graph_prefix 21
            # reaching created datas from db (main offer)

            primary_customer_id_tmp = return_cust_id_from_prefix(prefix1_tmp)

            secondary_customer_id_tmp = return_cust_id_from_prefix(prefix2_tmp)

            product_group_suppression_ih_check(primary_customer_id_tmp, secondary_customer_id_tmp, channel_tmp,
                                               subchannel_tmp, function_code_tmp,
                                               org_level_tmp, user_role_tmp, outcome_tmp, outcome_id_tmp, pyname_tmp,
                                               suppression_time_temp,
                                               suppress_channel_tmp, suppress_sub_channel_tmp,
                                               suppress_function_code_tmp, suppress_offer_pyname_tmp,
                                               suppress_org_level_tmp, suppress_user_role_tmp)
        elif test_case_tmp == "OfferSelfContention":
            # DATABASE CHECK EDİLİR DAHA ÖNCE KAYIT VAR MI KONTROL EDİLİR. MOBİLE/ CALLCENTER/ BRANCH
            # Write-IH yüzünden te record OLSUN dolasıyla function değişecek ih'ler gitmeyecek.
            offer_self_contention_ih_check_dif_channel(customer_id, channel_tmp, subchannel_tmp, function_code_tmp,
                                                       org_level_tmp, user_role_tmp, outcome_tmp, outcome_id_tmp,
                                                       pyname_tmp,
                                                       suppression_time_temp,
                                                       suppress_channel_tmp, suppress_sub_channel_tmp,
                                                       suppress_function_code_tmp, suppress_offer_pyname_tmp,
                                                       suppress_cdm_ref_id_tmp, suppress_product_group_id_tmp)
            # CDM-IH okay
            cross_offer_cdm_ih_check_dif_channel(customer_id, channel_tmp, subchannel_tmp, function_code_tmp,
                                                 org_level_tmp, user_role_tmp, outcome_tmp, outcome_id_tmp,
                                                 pyname_tmp,
                                                 suppression_time_temp,
                                                 suppress_channel_tmp, suppress_sub_channel_tmp,
                                                 suppress_function_code_tmp, suppress_offer_pyname_tmp,
                                                 suppress_cdm_ref_id_tmp, suppress_product_group_id_tmp)
            # getoffer request et ve teklifin geldiğini gör
            # Database check edilir.
            # Suppression day kadar geri alınır
            # Database check edilir.
            # getOffer tetiklenir teklifin gelmediği görülür.
            # Suppression day +1
            # Database check edilir.
            # getOffer tetiklenir teklifin geldiği görülür
            pass

        elif test_case_tmp == "ChannelSuppression":
            pass


if __name__ == '__main__':
    database = OracleDB()
    suppression_check()
    database.close_connection()
