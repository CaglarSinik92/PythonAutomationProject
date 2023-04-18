import datetime

from Servisler import GetOfferService
from Servisler import CaptureResponse
from datetime import date
import json


class ServiceProcess:

    def __init__(self):
        self.treatment_id = None
        self.interaction_id = None
        self.service_response = None
        self.is_offer_presented = False

    def getOfferResponse(self, cust_id, context_data, pyname):
        self.is_offer_presented = False
        data = {
            "PartyID": cust_id,
            "Context": context_data,
            "ContextFormat": "PlainText"
        }
        service = GetOfferService(
            "http://akbank-shippingtest.adqura.com/prweb/PRRestService/AdquraNBAServices/GetOffersWithContextV1"
            "/GetOffers",
            "caglar.sinik@adqura.com",
            "Akbank2026*",
            data
        )
        service.getOfferPost()
        self.service_response = json.loads(service.response.text)
        print(data)
        print(self.service_response)
        if 'Offers' in self.service_response:
            offers = self.service_response['Offers']
            for offer in offers:
                if offer["pyName"] == pyname:
                    self.is_offer_presented = True
                    interaction_id = self.service_response['InteractionID']
                    self.interaction_id = interaction_id
                    treatment_id = offer["TreatmentID"]
                    self.treatment_id = treatment_id

    def getOfferInteractionID(self):
        if 'Offers' in self.service_response:
            offers = self.service_response['Offers']
            for offer in offers:
                if offer["pyName"] == "IslekKredi_Branch":
                    if 'InteractionID' in self.service_response:
                        interaction_id = self.service_response['InteractionID']
                        self.interaction_id = interaction_id
                        break
                    else:
                        print("InteractionID değeri bulunamadı.")

    def getOfferTreatmentID(self):
        if 'Offers' in self.service_response:
            offers = self.service_response['Offers']
            for offer in offers:
                if offer["pyName"] == "IslekKredi_Branch":
                    treatment_id = offer["TreatmentID"]
                    self.treatment_id = treatment_id
                    break

    def captureResp(self, outcome, customer_id, responseCode, channel, functionCode):
        context_capture_resp = "responseDate==20230411T104500.000 GMT;;responseCode==" + responseCode + ";;reasonCode==C258;;channel==" + channel + ";;functionCode==" + functionCode + ";;offerType==X;;operationType==S;;customerInContact==false;;"
        if self.is_offer_presented:
            treatment_id = self.treatment_id
            interaction_id = self.interaction_id
            data = {
                "Outcome": outcome,
                "TreatmentID": treatment_id,
                "PartyID": customer_id,
                "InteractionID": interaction_id,
                "Context": context_capture_resp
            }
            service = CaptureResponse(
                "http://akbank-shippingtest.adqura.com/prweb/PRRestService/AdquraNBAServices/SetOutcomeV1/SetOutcome",
                "caglar.sinik@adqura.com", "Akbank2026*", data)
            service.captureResponse()
            data_json = json.loads(service.response.text)
            print(data)
            print(data_json)
        else:
            print("\nCaptureResponse NOT Triggered\n")

    # AssociatedOffer
    # offerType
    # TreatmentID
    # pyName
    # bannerId
    # CDMRefID
    # EndDate
    # StartDate
