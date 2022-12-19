from test.apiserver.test_agent_base import AgentTestCase


class ApiRouteTestCase(AgentTestCase):

    def test_agent_api_upload(self):
        data = {
            "detail": {
                "agentId":
                57,
                "apiData": [{
                    "controller": "",
                    "file": "",
                    "method": ["GET", "POST"],
                    "description": "",
                    "uri": "/orderbase/tagorder",
                    "class": "",
                    "parameters": "",
                    "returnType": ""
                }, {
                    "controller": "",
                    "file": "",
                    "method": ["GET", "POST"],
                    "description": "",
                    "uri": "/orderbase/queryvirtualnumber",
                    "class": "",
                    "parameters": "",
                    "returnType": ""
                }, {
                    "controller": "",
                    "file": "",
                    "method": ["GET", "POST"],
                    "description": "",
                    "uri": "/orderbase/confirmextrafeebydriver",
                    "class": "",
                    "parameters": "",
                    "returnType": ""
                }, {
                    "controller": "",
                    "file": "",
                    "method": ["GET", "POST"],
                    "description": "",
                    "uri": "/orderbase/queryorderforrecent24hoursbypassenger",
                    "class": "",
                    "parameters": "",
                    "returnType": ""
                }, {
                    "controller": "",
                    "file": "",
                    "method": ["GET", "POST"],
                    "description": "",
                    "uri": "/orderbase/queryorderbydemandno",
                    "class": "",
                    "parameters": "",
                    "returnType": ""
                }, {
                    "controller": "",
                    "file": "",
                    "method": ["GET", "POST"],
                    "description": "",
                    "uri": "/orderbase/pickup",
                    "class": "",
                    "parameters": "",
                    "returnType": ""
                }, {
                    "controller": "",
                    "file": "",
                    "method": ["GET", "POST"],
                    "description": "",
                    "uri": "/orderbase/getorderfeedetail",
                    "class": "",
                    "parameters": "",
                    "returnType": ""
                }, {
                    "controller": "",
                    "file": "",
                    "method": ["GET", "POST"],
                    "description": "",
                    "uri": "/orderbase/matchsucceed",
                    "class": "",
                    "parameters": "",
                    "returnType": ""
                }, {
                    "controller": "",
                    "file": "",
                    "method": ["GET", "POST"],
                    "description": "",
                    "uri": "/orderbase/arrive",
                    "class": "",
                    "parameters": "",
                    "returnType": ""
                }, {
                    "controller": "",
                    "file": "",
                    "method": ["GET", "POST"],
                    "description": "",
                    "uri": "/orderbase/startservice",
                    "class": "",
                    "parameters": "",
                    "returnType": ""
                }, {
                    "controller": "",
                    "file": "",
                    "method": ["GET", "POST"],
                    "description": "",
                    "uri": "/orderbase/recordsharechannel",
                    "class": "",
                    "parameters": "",
                    "returnType": ""
                }, {
                    "controller": "",
                    "file": "",
                    "method": ["GET", "POST"],
                    "description": "",
                    "uri": "/orderbase/arriveviapoint",
                    "class": "",
                    "parameters": "",
                    "returnType": ""
                }, {
                    "controller": "",
                    "file": "",
                    "method": ["GET", "POST"],
                    "description": "",
                    "uri": "/orderbase/drivercompleteorder",
                    "class": "",
                    "parameters": "",
                    "returnType": ""
                }, {
                    "controller": "",
                    "file": "",
                    "method": ["GET", "POST"],
                    "description": "",
                    "uri": "/orderbase/driverremindpayment",
                    "class": "",
                    "parameters": "",
                    "returnType": ""
                }, {
                    "controller": "",
                    "file": "",
                    "method": ["GET", "POST"],
                    "description": "",
                    "uri": "/orderbase/passengeruseinvitecode",
                    "class": "",
                    "parameters": "",
                    "returnType": ""
                }, {
                    "controller": "",
                    "file": "",
                    "method": ["GET", "POST"],
                    "description": "",
                    "uri": "/orderbase/updatedestinfo",
                    "class": "",
                    "parameters": "",
                    "returnType": ""
                }, {
                    "controller": "",
                    "file": "",
                    "method": ["GET", "POST"],
                    "description": "",
                    "uri": "/orderbase/updatepoibyorderno",
                    "class": "",
                    "parameters": "",
                    "returnType": ""
                }, {
                    "controller": "",
                    "file": "",
                    "method": ["GET", "POST"],
                    "description": "",
                    "uri": "/orderbase/queryreserveinfobydriver",
                    "class": "",
                    "parameters": "",
                    "returnType": ""
                }, {
                    "controller": "",
                    "file": "",
                    "method": ["GET", "POST"],
                    "description": "",
                    "uri": "/orderbase/queryeventchangebydriver",
                    "class": "",
                    "parameters": "",
                    "returnType": ""
                }, {
                    "controller": "",
                    "file": "",
                    "method": ["GET", "POST"],
                    "description": "",
                    "uri": "/orderbase/queryreservedispatchagaintask",
                    "class": "",
                    "parameters": "",
                    "returnType": ""
                }, {
                    "controller": "",
                    "file": "",
                    "method": ["GET", "POST"],
                    "description": "",
                    "uri": "/orderbase/queryorderdetail",
                    "class": "",
                    "parameters": "",
                    "returnType": ""
                }, {
                    "controller": "",
                    "file": "",
                    "method": ["GET", "POST"],
                    "description": "",
                    "uri": "/orderbase/querylastevent",
                    "class": "",
                    "parameters": "",
                    "returnType": ""
                }, {
                    "controller": "",
                    "file": "",
                    "method": ["GET", "POST"],
                    "description": "",
                    "uri": "/orderbase/redispatchorder",
                    "class": "",
                    "parameters": "",
                    "returnType": ""
                }, {
                    "controller": "",
                    "file": "",
                    "method": ["GET", "POST"],
                    "description": "",
                    "uri": "/orderbase/redispatchfailed",
                    "class": "",
                    "parameters": "",
                    "returnType": ""
                }, {
                    "controller": "",
                    "file": "",
                    "method": ["GET", "POST"],
                    "description": "",
                    "uri": "/orderbase/cancelredispatch",
                    "class": "",
                    "parameters": "",
                    "returnType": ""
                }, {
                    "controller": "",
                    "file": "",
                    "method": ["GET", "POST"],
                    "description": "",
                    "uri": "/orderbase/querylastredispatchstatus",
                    "class": "",
                    "parameters": "",
                    "returnType": ""
                }, {
                    "controller": "",
                    "file": "",
                    "method": ["GET", "POST"],
                    "description": "",
                    "uri": "/orderbase/queryredispatchhistory",
                    "class": "",
                    "parameters": "",
                    "returnType": ""
                }, {
                    "controller": "",
                    "file": "",
                    "method": ["GET", "POST"],
                    "description": "",
                    "uri": "/orderbase/arriveandsettlement",
                    "class": "",
                    "parameters": "",
                    "returnType": ""
                }, {
                    "controller": "",
                    "file": "",
                    "method": ["GET", "POST"],
                    "description": "",
                    "uri": "/orderbase/setcancelreasonbypassenger",
                    "class": "",
                    "parameters": "",
                    "returnType": ""
                }, {
                    "controller": "",
                    "file": "",
                    "method": ["GET", "POST"],
                    "description": "",
                    "uri": "/orderbase/unlockandcancelorder",
                    "class": "",
                    "parameters": "",
                    "returnType": ""
                }, {
                    "controller": "",
                    "file": "",
                    "method": ["GET", "POST"],
                    "description": "",
                    "uri": "/orderbase/ordereventnotifybymerchant",
                    "class": "",
                    "parameters": "",
                    "returnType": ""
                }, {
                    "controller": "",
                    "file": "",
                    "method": ["GET", "POST"],
                    "description": "",
                    "uri": "/orderbase/queryredispatchorders",
                    "class": "",
                    "parameters": "",
                    "returnType": ""
                }, {
                    "controller": "",
                    "file": "",
                    "method": ["GET", "POST"],
                    "description": "",
                    "uri": "/orderbase/applyredispatchorders",
                    "class": "",
                    "parameters": "",
                    "returnType": ""
                }, {
                    "controller": "",
                    "file": "",
                    "method": ["GET", "POST"],
                    "description": "",
                    "uri": "/orderbase/queryhistorycancelrule",
                    "class": "",
                    "parameters": "",
                    "returnType": ""
                }, {
                    "controller": "",
                    "file": "",
                    "method": ["GET", "POST"],
                    "description": "",
                    "uri": "/orderbase/queryflightchangehis",
                    "class": "",
                    "parameters": "",
                    "returnType": ""
                }, {
                    "controller": "",
                    "file": "",
                    "method": ["GET", "POST"],
                    "description": "",
                    "uri": "/orderbase/share",
                    "class": "",
                    "parameters": "",
                    "returnType": ""
                }, {
                    "controller": "",
                    "file": "",
                    "method": ["GET", "POST"],
                    "description": "",
                    "uri": "/orderbase/changedestination",
                    "class": "",
                    "parameters": "",
                    "returnType": ""
                }, {
                    "controller": "",
                    "file": "",
                    "method": ["GET", "POST"],
                    "description": "",
                    "uri": "/orderbase/modifyorderprice",
                    "class": "",
                    "parameters": "",
                    "returnType": ""
                }, {
                    "controller": "",
                    "file": "",
                    "method": ["GET", "POST"],
                    "description": "",
                    "uri": "/orderbase/changeflight",
                    "class": "",
                    "parameters": "",
                    "returnType": ""
                }, {
                    "controller": "",
                    "file": "",
                    "method": ["GET", "POST"],
                    "description": "",
                    "uri": "/orderbase/paybyplatformnotify",
                    "class": "",
                    "parameters": "",
                    "returnType": ""
                }, {
                    "controller": "",
                    "file": "",
                    "method": ["GET", "POST"],
                    "description": "",
                    "uri": "/orderbase/querycancelfeebymis",
                    "class": "",
                    "parameters": "",
                    "returnType": ""
                }, {
                    "controller": "",
                    "file": "",
                    "method": ["GET", "POST"],
                    "description": "",
                    "uri": "/orderbase/querycanceldisplay",
                    "class": "",
                    "parameters": "",
                    "returnType": ""
                }, {
                    "controller": "",
                    "file": "",
                    "method": ["GET", "POST"],
                    "description": "",
                    "uri": "/orderbase/arriveboardingpoint",
                    "class": "",
                    "parameters": "",
                    "returnType": ""
                }, {
                    "controller": "",
                    "file": "",
                    "method": ["GET", "POST"],
                    "description": "",
                    "uri": "/orderbase/cancelorder",
                    "class": "",
                    "parameters": "",
                    "returnType": ""
                }, {
                    "controller": "",
                    "file": "",
                    "method": ["GET", "POST"],
                    "description": "",
                    "uri": "/orderbase/queryorders",
                    "class": "",
                    "parameters": "",
                    "returnType": ""
                }, {
                    "controller": "",
                    "file": "",
                    "method": ["GET", "POST"],
                    "description": "",
                    "uri": "/orderbase/queryredispatchingorderbydriver",
                    "class": "",
                    "parameters": "",
                    "returnType": ""
                }, {
                    "controller": "",
                    "file": "",
                    "method": ["GET", "POST"],
                    "description": "",
                    "uri": "/orderbase/querydriverredispatchcount",
                    "class": "",
                    "parameters": "",
                    "returnType": ""
                }, {
                    "controller": "",
                    "file": "",
                    "method": ["GET", "POST"],
                    "description": "",
                    "uri": "/orderbase/deleteorderbydriver",
                    "class": "",
                    "parameters": "",
                    "returnType": ""
                }, {
                    "controller": "",
                    "file": "",
                    "method": ["GET", "POST"],
                    "description": "",
                    "uri": "/orderbase/deleteorderbypassenger",
                    "class": "",
                    "parameters": "",
                    "returnType": ""
                }, {
                    "controller": "",
                    "file": "",
                    "method": ["GET", "POST"],
                    "description": "",
                    "uri": "/orderbase/cancelorderbymis",
                    "class": "",
                    "parameters": "",
                    "returnType": ""
                }, {
                    "controller": "",
                    "file": "",
                    "method": ["GET", "POST"],
                    "description": "",
                    "uri": "/orderbase/queryorderchainlist",
                    "class": "",
                    "parameters": "",
                    "returnType": ""
                }, {
                    "controller": "",
                    "file": "",
                    "method": ["GET", "POST"],
                    "description": "",
                    "uri": "/orderbase/queryvehicleinfobypassenger",
                    "class": "",
                    "parameters": "",
                    "returnType": ""
                }, {
                    "controller": "",
                    "file": "",
                    "method": ["GET", "POST"],
                    "description": "",
                    "uri": "/orderbase/querylatestorder",
                    "class": "",
                    "parameters": "",
                    "returnType": ""
                }, {
                    "controller": "",
                    "file": "",
                    "method": ["GET", "POST"],
                    "description": "",
                    "uri": "/orderbase/confirmordersettlement",
                    "class": "",
                    "parameters": "",
                    "returnType": ""
                }, {
                    "controller": "",
                    "file": "",
                    "method": ["GET", "POST"],
                    "description": "",
                    "uri": "/orderbase/premodifyorderprice",
                    "class": "",
                    "parameters": "",
                    "returnType": ""
                }, {
                    "controller": "",
                    "file": "",
                    "method": ["GET", "POST"],
                    "description": "",
                    "uri": "/orderbase/queryreservestartordersbydriver",
                    "class": "",
                    "parameters": "",
                    "returnType": ""
                }, {
                    "controller": "",
                    "file": "",
                    "method": ["GET", "POST"],
                    "description": "",
                    "uri": "/orderbase/paynotify",
                    "class": "",
                    "parameters": "",
                    "returnType": ""
                }, {
                    "controller": "",
                    "file": "",
                    "method": ["GET", "POST"],
                    "description": "",
                    "uri": "/orderbase/createpayorder",
                    "class": "",
                    "parameters": "",
                    "returnType": ""
                }, {
                    "controller": "",
                    "file": "",
                    "method": ["GET", "POST"],
                    "description": "",
                    "uri": "/orderbase/checkchangedestinationpayadvance",
                    "class": "",
                    "parameters": "",
                    "returnType": ""
                }, {
                    "controller": "",
                    "file": "",
                    "method": ["GET", "POST"],
                    "description": "",
                    "uri": "/orderbase/cancelpayorder",
                    "class": "",
                    "parameters": "",
                    "returnType": ""
                }, {
                    "controller": "",
                    "file": "",
                    "method": ["GET", "POST"],
                    "description": "",
                    "uri": "/orderbase/checkchangedestination",
                    "class": "",
                    "parameters": "",
                    "returnType": ""
                }, {
                    "controller": "",
                    "file": "",
                    "method": ["GET", "POST"],
                    "description": "",
                    "uri": "/orderbase/canceldriverservice",
                    "class": "",
                    "parameters": "",
                    "returnType": ""
                }, {
                    "controller": "",
                    "file": "",
                    "method": ["GET", "POST"],
                    "description": "",
                    "uri": "/orderbase/prerefund",
                    "class": "",
                    "parameters": "",
                    "returnType": ""
                }, {
                    "controller": "",
                    "file": "",
                    "method": ["GET", "POST"],
                    "description": "",
                    "uri": "/orderbase/refund",
                    "class": "",
                    "parameters": "",
                    "returnType": ""
                }, {
                    "controller": "",
                    "file": "",
                    "method": ["GET", "POST"],
                    "description": "",
                    "uri": "/orderbase/unifiedrefundnotify",
                    "class": "",
                    "parameters": "",
                    "returnType": ""
                }, {
                    "controller": "",
                    "file": "",
                    "method": ["GET", "POST"],
                    "description": "",
                    "uri": "/orderbase/prededuct",
                    "class": "",
                    "parameters": "",
                    "returnType": ""
                }, {
                    "controller": "",
                    "file": "",
                    "method": ["GET", "POST"],
                    "description": "",
                    "uri": "/orderbase/deduct",
                    "class": "",
                    "parameters": "",
                    "returnType": ""
                }, {
                    "controller": "",
                    "file": "",
                    "method": ["GET", "POST"],
                    "description": "",
                    "uri": "/orderbase/queryconflictorderlist",
                    "class": "",
                    "parameters": "",
                    "returnType": ""
                }, {
                    "controller": "",
                    "file": "",
                    "method": ["GET", "POST"],
                    "description": "",
                    "uri": "/orderbase/querycacheorderinfo",
                    "class": "",
                    "parameters": "",
                    "returnType": ""
                }, {
                    "controller": "",
                    "file": "",
                    "method": ["GET", "POST"],
                    "description": "",
                    "uri": "/orderbase/querylastreservebydriver",
                    "class": "",
                    "parameters": "",
                    "returnType": ""
                }, {
                    "controller": "",
                    "file": "",
                    "method": ["GET", "POST"],
                    "description": "",
                    "uri": "/orderbase/refuseorderbydriver",
                    "class": "",
                    "parameters": "",
                    "returnType": ""
                }, {
                    "controller": "",
                    "file": "",
                    "method": ["GET", "POST"],
                    "description": "",
                    "uri": "/orderbase/queryuserguidecancelrule",
                    "class": "",
                    "parameters": "",
                    "returnType": ""
                }, {
                    "controller": "",
                    "file": "",
                    "method": ["GET", "POST"],
                    "description": "",
                    "uri": "/orderbase/querycancelledorder",
                    "class": "",
                    "parameters": "",
                    "returnType": ""
                }, {
                    "controller": "",
                    "file": "",
                    "method": ["GET", "POST"],
                    "description": "",
                    "uri": "/orderbase/queryunstartreservelistbydriver",
                    "class": "",
                    "parameters": "",
                    "returnType": ""
                }, {
                    "controller": "",
                    "file": "",
                    "method": ["GET", "POST"],
                    "description": "",
                    "uri": "/orderbase/refunddetail",
                    "class": "",
                    "parameters": "",
                    "returnType": ""
                }, {
                    "controller": "",
                    "file": "",
                    "method": ["GET", "POST"],
                    "description": "",
                    "uri": "/orderbase/autopaybyplatformnotify",
                    "class": "",
                    "parameters": "",
                    "returnType": ""
                }, {
                    "controller": "",
                    "file": "",
                    "method": ["GET", "POST"],
                    "description": "",
                    "uri": "/orderbase/confirmextrafeebypassenger",
                    "class": "",
                    "parameters": "",
                    "returnType": ""
                }, {
                    "controller": "",
                    "file": "",
                    "method": ["GET", "POST"],
                    "description": "",
                    "uri": "/orderbase/enterviapoint",
                    "class": "",
                    "parameters": "",
                    "returnType": ""
                }, {
                    "controller": "",
                    "file": "",
                    "method": ["GET", "POST"],
                    "description": "",
                    "uri": "/orderbase/exitviapoint",
                    "class": "",
                    "parameters": "",
                    "returnType": ""
                }, {
                    "controller": "",
                    "file": "",
                    "method": ["GET", "POST"],
                    "description": "",
                    "uri": "/orderbase/arriveddestpartition",
                    "class": "",
                    "parameters": "",
                    "returnType": ""
                }, {
                    "controller": "",
                    "file": "",
                    "method": ["GET", "POST"],
                    "description": "",
                    "uri": "/orderbase/refunddetaillist",
                    "class": "",
                    "parameters": "",
                    "returnType": ""
                }, {
                    "controller": "",
                    "file": "",
                    "method": ["GET", "POST"],
                    "description": "",
                    "uri": "/orderbase/deductdetaillist",
                    "class": "",
                    "parameters": "",
                    "returnType": ""
                }, {
                    "controller": "",
                    "file": "",
                    "method": ["GET", "POST"],
                    "description": "",
                    "uri": "/orderbase/savecachedata",
                    "class": "",
                    "parameters": "",
                    "returnType": ""
                }, {
                    "controller": "",
                    "file": "",
                    "method": ["GET", "POST"],
                    "description": "",
                    "uri": "/orderbase/getcachedata",
                    "class": "",
                    "parameters": "",
                    "returnType": ""
                }, {
                    "controller": "",
                    "file": "",
                    "method": ["GET", "POST"],
                    "description": "",
                    "uri": "/orderbase/getviapointsbyordernos",
                    "class": "",
                    "parameters": "",
                    "returnType": ""
                }, {
                    "controller": "",
                    "file": "",
                    "method": ["GET", "POST"],
                    "description": "",
                    "uri": "/orderbase/getpaymentsbyordernos",
                    "class": "",
                    "parameters": "",
                    "returnType": ""
                }, {
                    "controller": "",
                    "file": "",
                    "method": ["GET", "POST"],
                    "description": "",
                    "uri": "/orderbase/querypaymentinfobyorderno",
                    "class": "",
                    "parameters": "",
                    "returnType": ""
                }, {
                    "controller": "",
                    "file": "",
                    "method": ["GET", "POST"],
                    "description": "",
                    "uri": "/orderbase/querymodifypriceinfobyorderno",
                    "class": "",
                    "parameters": "",
                    "returnType": ""
                }, {
                    "controller": "",
                    "file": "",
                    "method": ["GET", "POST"],
                    "description": "",
                    "uri": "/orderbase/getpartitionsbyorderno",
                    "class": "",
                    "parameters": "",
                    "returnType": ""
                }, {
                    "controller": "",
                    "file": "",
                    "method": ["GET", "POST"],
                    "description": "",
                    "uri": "/orderbase/receivealarm",
                    "class": "",
                    "parameters": "",
                    "returnType": ""
                }, {
                    "controller": "",
                    "file": "",
                    "method": ["GET", "POST"],
                    "description": "",
                    "uri": "/orderbase/querypayadvanceinfo",
                    "class": "",
                    "parameters": "",
                    "returnType": ""
                }, {
                    "controller": "",
                    "file": "",
                    "method": ["GET", "POST"],
                    "description": "",
                    "uri": "/orderbase/queryorderbypartner",
                    "class": "",
                    "parameters": "",
                    "returnType": ""
                }, {
                    "controller": "",
                    "file": "",
                    "method": ["GET", "POST"],
                    "description": "",
                    "uri": "/orderbase/cancelorderbytest",
                    "class": "",
                    "parameters": "",
                    "returnType": ""
                }, {
                    "controller": "",
                    "file": "",
                    "method": ["GET", "POST"],
                    "description": "",
                    "uri": "/orderbase/querysettlementdetailbycharter",
                    "class": "",
                    "parameters": "",
                    "returnType": ""
                }, {
                    "controller": "",
                    "file": "",
                    "method": ["GET", "POST"],
                    "description": "",
                    "uri": "/orderbase/querymodifypriceandrefundamount",
                    "class": "",
                    "parameters": "",
                    "returnType": ""
                }, {
                    "controller": "",
                    "file": "",
                    "method": ["GET", "POST"],
                    "description": "",
                    "uri": "/orderbase/querysettlementdetailbycharterv2",
                    "class": "",
                    "parameters": "",
                    "returnType": ""
                }, {
                    "controller": "",
                    "file": "",
                    "method": ["GET", "POST"],
                    "description": "",
                    "uri": "/orderbase/confirmordersettlementbycharter",
                    "class": "",
                    "parameters": "",
                    "returnType": ""
                }, {
                    "controller": "",
                    "file": "",
                    "method": ["GET", "POST"],
                    "description": "",
                    "uri": "/orderbase/cancelorderbydriver",
                    "class": "",
                    "parameters": "",
                    "returnType": ""
                }, {
                    "controller": "",
                    "file": "",
                    "method": ["GET", "POST"],
                    "description": "",
                    "uri": "/orderbase/queryorderfeedetail",
                    "class": "",
                    "parameters": "",
                    "returnType": ""
                }, {
                    "controller": "",
                    "file": "",
                    "method": ["GET", "POST"],
                    "description": "",
                    "uri": "/orderbase/uploadnavigationchange",
                    "class": "",
                    "parameters": "",
                    "returnType": ""
                }, {
                    "controller": "",
                    "file": "",
                    "method": ["GET", "POST"],
                    "description": "",
                    "uri": "/orderbase/queryexceptionorder",
                    "class": "",
                    "parameters": "",
                    "returnType": ""
                }, {
                    "controller": "",
                    "file": "",
                    "method": ["GET", "POST"],
                    "description": "",
                    "uri": "/orderbase/querynavigationchangelog",
                    "class": "",
                    "parameters": "",
                    "returnType": ""
                }, {
                    "controller": "",
                    "file": "",
                    "method": ["GET", "POST"],
                    "description": "",
                    "uri": "/orderbase/addequity",
                    "class": "",
                    "parameters": "",
                    "returnType": ""
                }, {
                    "controller": "",
                    "file": "",
                    "method": ["GET", "POST"],
                    "description": "",
                    "uri": "/orderbase/preredispatchfailed",
                    "class": "",
                    "parameters": "",
                    "returnType": ""
                }, {
                    "controller": "",
                    "file": "",
                    "method": ["GET", "POST"],
                    "description": "",
                    "uri": "/orderbase/statordersdailydriver",
                    "class": "",
                    "parameters": "",
                    "returnType": ""
                }, {
                    "controller": "",
                    "file": "",
                    "method": ["GET", "POST"],
                    "description": "",
                    "uri": "/orderbase/stopwork",
                    "class": "",
                    "parameters": "",
                    "returnType": ""
                }, {
                    "controller": "",
                    "file": "",
                    "method": ["GET", "POST"],
                    "description": "",
                    "uri": "/orderbase/deleteorder",
                    "class": "",
                    "parameters": "",
                    "returnType": ""
                }, {
                    "controller": "",
                    "file": "",
                    "method": ["GET", "POST"],
                    "description": "",
                    "uri": "/orderbase/querytaskinfo",
                    "class": "",
                    "parameters": "",
                    "returnType": ""
                }, {
                    "controller": "",
                    "file": "",
                    "method": ["GET", "POST"],
                    "description": "",
                    "uri": "/orderbase/queryselfunfinishorderlist",
                    "class": "",
                    "parameters": "",
                    "returnType": ""
                }, {
                    "controller": "",
                    "file": "",
                    "method": ["GET", "POST"],
                    "description": "",
                    "uri": "/orderbase/pushmerchantorderstatus",
                    "class": "",
                    "parameters": "",
                    "returnType": ""
                }, {
                    "controller": "",
                    "file": "",
                    "method": ["GET", "POST"],
                    "description": "",
                    "uri": "/orderbase/resetorder",
                    "class": "",
                    "parameters": "",
                    "returnType": ""
                }, {
                    "controller": "",
                    "file": "",
                    "method": ["GET", "POST"],
                    "description": "",
                    "uri": "/orderbase/updatestatus",
                    "class": "",
                    "parameters": "",
                    "returnType": ""
                }, {
                    "controller": "",
                    "file": "",
                    "method": ["GET", "POST"],
                    "description": "",
                    "uri": "/orderbase/matchsucceedv2",
                    "class": "",
                    "parameters": "",
                    "returnType": ""
                }, {
                    "controller": "",
                    "file": "",
                    "method": ["GET", "POST"],
                    "description": "",
                    "uri": "/orderbase/getdemandorsupplyorder",
                    "class": "",
                    "parameters": "",
                    "returnType": ""
                }, {
                    "controller": "",
                    "file": "",
                    "method": ["GET", "POST"],
                    "description": "",
                    "uri": "/orderbase/cancelorderforextsupply",
                    "class": "",
                    "parameters": "",
                    "returnType": ""
                }, {
                    "controller": "",
                    "file": "",
                    "method": ["GET", "POST"],
                    "description": "",
                    "uri": "/orderbase/operateordertag",
                    "class": "",
                    "parameters": "",
                    "returnType": ""
                }, {
                    "controller": "",
                    "file": "",
                    "method": ["GET", "POST"],
                    "description": "",
                    "uri": "/orderbase/querycancelordertag",
                    "class": "",
                    "parameters": "",
                    "returnType": ""
                }, {
                    "controller": "",
                    "file": "",
                    "method": ["GET", "POST"],
                    "description": "",
                    "uri": "/orderbase/querypassengerstat",
                    "class": "",
                    "parameters": "",
                    "returnType": ""
                }, {
                    "controller": "",
                    "file": "",
                    "method": ["GET", "POST"],
                    "description": "",
                    "uri": "/orderbase/freeorderbyplatform",
                    "class": "",
                    "parameters": "",
                    "returnType": ""
                }, {
                    "controller": "",
                    "file": "",
                    "method": ["GET", "POST"],
                    "description": "",
                    "uri": "/orderbase/queryorderbymisback",
                    "class": "",
                    "parameters": "",
                    "returnType": ""
                }, {
                    "controller": "",
                    "file": "",
                    "method": ["GET", "POST"],
                    "description": "",
                    "uri": "/orderbase/receivealarmforzebra",
                    "class": "",
                    "parameters": "",
                    "returnType": ""
                }, {
                    "controller": "",
                    "file": "",
                    "method": ["GET", "POST"],
                    "description": "",
                    "uri": "/orderbase/inserttaskinfo",
                    "class": "",
                    "parameters": "",
                    "returnType": ""
                }, {
                    "controller": "",
                    "file": "",
                    "method": ["GET", "POST"],
                    "description": "",
                    "uri": "/orderbase/queryunfinishedordersbydriver",
                    "class": "",
                    "parameters": "",
                    "returnType": ""
                }, {
                    "controller": "",
                    "file": "",
                    "method": ["GET", "POST"],
                    "description": "",
                    "uri": "/orderbase/cancelreleasehandle",
                    "class": "",
                    "parameters": "",
                    "returnType": ""
                }, {
                    "controller": "",
                    "file": "",
                    "method": ["GET", "POST"],
                    "description": "",
                    "uri": "/orderbase/querycancelrelease",
                    "class": "",
                    "parameters": "",
                    "returnType": ""
                }, {
                    "controller": "",
                    "file": "",
                    "method": ["GET", "POST"],
                    "description": "",
                    "uri": "/orderbase/redispatchorderbymis",
                    "class": "",
                    "parameters": "",
                    "returnType": ""
                }, {
                    "controller": "",
                    "file": "",
                    "method": ["GET", "POST"],
                    "description": "",
                    "uri": "/orderbase/createpayorderandpushpassenger",
                    "class": "",
                    "parameters": "",
                    "returnType": ""
                }, {
                    "controller": "",
                    "file": "",
                    "method": ["GET", "POST"],
                    "description": "",
                    "uri": "/orderbase/sendorderurl",
                    "class": "",
                    "parameters": "",
                    "returnType": ""
                }, {
                    "controller": "",
                    "file": "",
                    "method": ["GET", "POST"],
                    "description": "",
                    "uri": "/orderbase/unifiedtaskexecution",
                    "class": "",
                    "parameters": "",
                    "returnType": ""
                }, {
                    "controller": "",
                    "file": "",
                    "method": ["GET", "POST"],
                    "description": "",
                    "uri": "/orderbase/commitrefund",
                    "class": "",
                    "parameters": "",
                    "returnType": ""
                }, {
                    "controller": "",
                    "file": "",
                    "method": ["GET", "POST"],
                    "description": "",
                    "uri": "/orderbase/checkfirstsettlement",
                    "class": "",
                    "parameters": "",
                    "returnType": ""
                }, {
                    "controller": "",
                    "file": "",
                    "method": ["GET", "POST"],
                    "description": "",
                    "uri": "/orderbase/queryrelationorders",
                    "class": "",
                    "parameters": "",
                    "returnType": ""
                }, {
                    "controller": "",
                    "file": "",
                    "method": ["GET", "POST"],
                    "description": "",
                    "uri": "/orderbase/urgentsettlement",
                    "class": "",
                    "parameters": "",
                    "returnType": ""
                }, {
                    "controller": "",
                    "file": "",
                    "method": ["GET", "POST"],
                    "description": "",
                    "uri": "/orderbase/savefeerelease",
                    "class": "",
                    "parameters": "",
                    "returnType": ""
                }, {
                    "controller": "",
                    "file": "",
                    "method": ["GET", "POST"],
                    "description": "",
                    "uri": "/orderbase/getfeerelease",
                    "class": "",
                    "parameters": "",
                    "returnType": ""
                }, {
                    "controller": "",
                    "file": "",
                    "method": ["GET", "POST"],
                    "description": "",
                    "uri": "/orderbase/closeparentorder",
                    "class": "",
                    "parameters": "",
                    "returnType": ""
                }, {
                    "controller": "",
                    "file": "",
                    "method": ["GET", "POST"],
                    "description": "",
                    "uri": "/orderbase/refundrollback",
                    "class": "",
                    "parameters": "",
                    "returnType": ""
                }, {
                    "controller": "",
                    "file": "",
                    "method": ["GET", "POST"],
                    "description": "",
                    "uri": "/orderbase/queryorderlistbydevice",
                    "class": "",
                    "parameters": "",
                    "returnType": ""
                }, {
                    "controller": "",
                    "file": "",
                    "method": ["GET", "POST"],
                    "description": "",
                    "uri": "/orderbase/countfeereleasebyuid",
                    "class": "",
                    "parameters": "",
                    "returnType": ""
                }, {
                    "controller": "",
                    "file": "",
                    "method": ["GET", "POST"],
                    "description": "",
                    "uri": "/orderbase/querydriverappealunreadcount",
                    "class": "",
                    "parameters": "",
                    "returnType": ""
                }, {
                    "controller": "",
                    "file": "",
                    "method": ["GET", "POST"],
                    "description": "",
                    "uri": "/orderbase/editdriverappealunread",
                    "class": "",
                    "parameters": "",
                    "returnType": ""
                }, {
                    "controller": "",
                    "file": "",
                    "method": ["GET", "POST"],
                    "description": "",
                    "uri": "/orderbase/querydriverappeallist",
                    "class": "",
                    "parameters": "",
                    "returnType": ""
                }, {
                    "controller": "",
                    "file": "",
                    "method": ["GET", "POST"],
                    "description": "",
                    "uri": "/orderbase/querydriverappealdetail",
                    "class": "",
                    "parameters": "",
                    "returnType": ""
                }, {
                    "controller": "",
                    "file": "",
                    "method": ["GET", "POST"],
                    "description": "",
                    "uri": "/orderbase/driverappealcheck",
                    "class": "",
                    "parameters": "",
                    "returnType": ""
                }, {
                    "controller": "",
                    "file": "",
                    "method": ["GET", "POST"],
                    "description": "",
                    "uri": "/orderbase/driverappealsave",
                    "class": "",
                    "parameters": "",
                    "returnType": ""
                }, {
                    "controller": "",
                    "file": "",
                    "method": ["GET", "POST"],
                    "description": "",
                    "uri": "/orderbase/querydrivercashreward",
                    "class": "",
                    "parameters": "",
                    "returnType": ""
                }, {
                    "controller": "",
                    "file": "",
                    "method": ["GET", "POST"],
                    "description": "",
                    "uri": "/orderbase/senddrivercashreward",
                    "class": "",
                    "parameters": "",
                    "returnType": ""
                }, {
                    "controller": "",
                    "file": "",
                    "method": ["GET", "POST"],
                    "description": "",
                    "uri": "/orderbase/paymentconfirm",
                    "class": "",
                    "parameters": "",
                    "returnType": ""
                }, {
                    "controller": "",
                    "file": "",
                    "method": ["GET", "POST"],
                    "description": "",
                    "uri": "/orderbase/updatepassengersurveyflag",
                    "class": "",
                    "parameters": "",
                    "returnType": ""
                }, {
                    "controller": "",
                    "file": "",
                    "method": ["GET", "POST"],
                    "description": "",
                    "uri": "/orderbase/synclocaldata",
                    "class": "",
                    "parameters": "",
                    "returnType": ""
                }, {
                    "controller": "",
                    "file": "",
                    "method": ["GET", "POST"],
                    "description": "",
                    "uri": "/orderbase/changedestinationconfirm",
                    "class": "",
                    "parameters": "",
                    "returnType": ""
                }, {
                    "controller": "",
                    "file": "",
                    "method": ["GET", "POST"],
                    "description": "",
                    "uri": "/orderbase/saveordertransinner",
                    "class": "",
                    "parameters": "",
                    "returnType": ""
                }, {
                    "controller": "",
                    "file": "",
                    "method": ["GET", "POST"],
                    "description": "",
                    "uri": "/orderbase/changeorigin",
                    "class": "",
                    "parameters": "",
                    "returnType": ""
                }, {
                    "controller": "",
                    "file": "",
                    "method": ["GET", "POST"],
                    "description": "",
                    "uri": "/orderbase/changeroute",
                    "class": "",
                    "parameters": "",
                    "returnType": ""
                }, {
                    "controller": "",
                    "file": "",
                    "method": ["GET", "POST"],
                    "description": "",
                    "uri": "/orderbase/prepayrefundnotify",
                    "class": "",
                    "parameters": "",
                    "returnType": ""
                }, {
                    "controller": "",
                    "file": "",
                    "method": ["GET", "POST"],
                    "description": "",
                    "uri": "/orderbase/paychannelchangenotify",
                    "class": "",
                    "parameters": "",
                    "returnType": ""
                }, {
                    "controller": "",
                    "file": "",
                    "method": ["GET", "POST"],
                    "description": "",
                    "uri": "/orderbase/querynextorderlist",
                    "class": "",
                    "parameters": "",
                    "returnType": ""
                }, {
                    "controller": "",
                    "file": "",
                    "method": ["GET", "POST"],
                    "description": "",
                    "uri": "/orderbase/uploaddrivingsituation",
                    "class": "",
                    "parameters": "",
                    "returnType": ""
                }, {
                    "controller": "",
                    "file": "",
                    "method": ["GET", "POST"],
                    "description": "",
                    "uri": "/orderbase/updateordertag",
                    "class": "",
                    "parameters": "",
                    "returnType": ""
                }, {
                    "controller": "",
                    "file": "",
                    "method": ["GET", "POST"],
                    "description": "",
                    "uri": "/orderbase/changecarusetime",
                    "class": "",
                    "parameters": "",
                    "returnType": ""
                }, {
                    "controller": "",
                    "file": "",
                    "method": ["GET", "POST"],
                    "description": "",
                    "uri": "/orderbase/changecarusetimeconfirm",
                    "class": "",
                    "parameters": "",
                    "returnType": ""
                }, {
                    "controller": "",
                    "file": "",
                    "method": ["GET", "POST"],
                    "description": "",
                    "uri": "/orderbase/markexception",
                    "class": "",
                    "parameters": "",
                    "returnType": ""
                }, {
                    "controller": "",
                    "file": "",
                    "method": ["GET", "POST"],
                    "description": "",
                    "uri": "/orderbase/changeroutecheck",
                    "class": "",
                    "parameters": "",
                    "returnType": ""
                }, {
                    "controller": "",
                    "file": "",
                    "method": ["GET", "POST"],
                    "description": "",
                    "uri": "/orderbase/updateaftersalesmodel",
                    "class": "",
                    "parameters": "",
                    "returnType": ""
                }, {
                    "controller": "",
                    "file": "",
                    "method": ["GET", "POST"],
                    "description": "",
                    "uri": "/orderbase/insuranceresultnotify",
                    "class": "",
                    "parameters": "",
                    "returnType": ""
                }, {
                    "controller": "",
                    "file": "",
                    "method": ["GET", "POST"],
                    "description": "",
                    "uri": "/orderbase/removelocalcachedata",
                    "class": "",
                    "parameters": "",
                    "returnType": ""
                }, {
                    "controller": "",
                    "file": "",
                    "method": ["GET", "POST"],
                    "description": "",
                    "uri": "/orderbase/querycanceltask",
                    "class": "",
                    "parameters": "",
                    "returnType": ""
                }, {
                    "controller": "",
                    "file": "",
                    "method": ["GET", "POST"],
                    "description": "",
                    "uri": "/orderbase/getordernobymockcode",
                    "class": "",
                    "parameters": "",
                    "returnType": ""
                }, {
                    "controller": "",
                    "file": "",
                    "method": ["GET", "POST"],
                    "description": "",
                    "uri": "/orderbase/getuserreport",
                    "class": "",
                    "parameters": "",
                    "returnType": ""
                }, {
                    "controller": "",
                    "file": "",
                    "method": ["GET", "POST"],
                    "description": "",
                    "uri": "/orderbase/updatedrivertag",
                    "class": "",
                    "parameters": "",
                    "returnType": ""
                }, {
                    "controller": "",
                    "file": "",
                    "method": ["GET", "POST"],
                    "description": "",
                    "uri": "/orderbase/gettripremarkform",
                    "class": "",
                    "parameters": "",
                    "returnType": ""
                }, {
                    "controller": "",
                    "file": "",
                    "method": ["GET", "POST"],
                    "description": "",
                    "uri": "/orderbase/gettripremarkresult",
                    "class": "",
                    "parameters": "",
                    "returnType": ""
                }, {
                    "controller": "",
                    "file": "",
                    "method": ["GET", "POST"],
                    "description": "",
                    "uri": "/orderbase/updatetripremarkresult",
                    "class": "",
                    "parameters": "",
                    "returnType": ""
                }, {
                    "controller": "",
                    "file": "",
                    "method": ["GET", "POST"],
                    "description": "",
                    "uri": "/orderbase/gettripremarklist",
                    "class": "",
                    "parameters": "",
                    "returnType": ""
                }, {
                    "controller": "",
                    "file": "",
                    "method": ["GET", "POST"],
                    "description": "",
                    "uri": "/orderbase/getcontactchangelist",
                    "class": "",
                    "parameters": "",
                    "returnType": ""
                }, {
                    "controller": "",
                    "file": "",
                    "method": ["GET", "POST"],
                    "description": "",
                    "uri": "/orderbase/changecontact",
                    "class": "",
                    "parameters": "",
                    "returnType": ""
                }, {
                    "controller": "",
                    "file": "",
                    "method": ["GET", "POST"],
                    "description": "",
                    "uri": "/orderbase/queryorderstatus4price",
                    "class": "",
                    "parameters": "",
                    "returnType": ""
                }]
            },
            "type": 97
        }
        data['detail']['agentId'] = self.agent_id
        res = self.agent_report(data, agentId=self.agent_id)
