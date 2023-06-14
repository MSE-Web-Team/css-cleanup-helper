import pandas as pd
import matplotlib.pyplot as plt

d = {
    "data": [
        {
            "family_contribution": 1639,
            "need_based_score": 25,
            "applicant_sid": "89283"
        },
        {
            "family_contribution": 148971,
            "need_based_score": 6,
            "applicant_sid": "89284"
        },
        {
            "family_contribution": 0,
            "need_based_score": 22,
            "applicant_sid": "89285"
        },
        {
            "family_contribution": 29507,
            "need_based_score": 10,
            "applicant_sid": "89286"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -19,
            "applicant_sid": "89287"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -19,
            "applicant_sid": "89288"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -19,
            "applicant_sid": "89289"
        },
        {
            "family_contribution": 1537,
            "need_based_score": 21,
            "applicant_sid": "89290"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -19,
            "applicant_sid": "89291"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -19,
            "applicant_sid": "89292"
        },
        {
            "family_contribution": 41218,
            "need_based_score": 11,
            "applicant_sid": "89293"
        },
        {
            "family_contribution": 55527,
            "need_based_score": 6,
            "applicant_sid": "89294"
        },
        {
            "family_contribution": 6547,
            "need_based_score": 14,
            "applicant_sid": "89295"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -19,
            "applicant_sid": "89296"
        },
        {
            "family_contribution": 0,
            "need_based_score": 25,
            "applicant_sid": "89297"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -16,
            "applicant_sid": "89298"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -20,
            "applicant_sid": "89299"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -16,
            "applicant_sid": "89300"
        },
        {
            "family_contribution": 2180,
            "need_based_score": 22,
            "applicant_sid": "89301"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -20,
            "applicant_sid": "89302"
        },
        {
            "family_contribution": 45800,
            "need_based_score": 8,
            "applicant_sid": "89303"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -19,
            "applicant_sid": "89304"
        },
        {
            "family_contribution": 16990,
            "need_based_score": 8,
            "applicant_sid": "89305"
        },
        {
            "family_contribution": 33,
            "need_based_score": 23,
            "applicant_sid": "89306"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -23,
            "applicant_sid": "89307"
        },
        {
            "family_contribution": 11413,
            "need_based_score": 13,
            "applicant_sid": "89308"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -16,
            "applicant_sid": "89309"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -20,
            "applicant_sid": "89310"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -16,
            "applicant_sid": "89311"
        },
        {
            "family_contribution": 0,
            "need_based_score": 25,
            "applicant_sid": "89312"
        },
        {
            "family_contribution": 3730,
            "need_based_score": 25,
            "applicant_sid": "89313"
        },
        {
            "family_contribution": 3187,
            "need_based_score": 21,
            "applicant_sid": "89314"
        },
        {
            "family_contribution": 87027,
            "need_based_score": 7,
            "applicant_sid": "89315"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -16,
            "applicant_sid": "89316"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -17,
            "applicant_sid": "89317"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -19,
            "applicant_sid": "89318"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -19,
            "applicant_sid": "89319"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -24,
            "applicant_sid": "89320"
        },
        {
            "family_contribution": 8235,
            "need_based_score": 17,
            "applicant_sid": "89321"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -19,
            "applicant_sid": "89322"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -19,
            "applicant_sid": "89323"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -16,
            "applicant_sid": "89324"
        },
        {
            "family_contribution": 0,
            "need_based_score": 22,
            "applicant_sid": "89325"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -20,
            "applicant_sid": "89326"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -16,
            "applicant_sid": "89327"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -16,
            "applicant_sid": "89328"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -16,
            "applicant_sid": "89329"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -16,
            "applicant_sid": "89330"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -21,
            "applicant_sid": "89331"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -22,
            "applicant_sid": "89332"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -14,
            "applicant_sid": "89333"
        },
        {
            "family_contribution": 9794,
            "need_based_score": 14,
            "applicant_sid": "89334"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -16,
            "applicant_sid": "89335"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -16,
            "applicant_sid": "89336"
        },
        {
            "family_contribution": 351122,
            "need_based_score": 5,
            "applicant_sid": "89337"
        },
        {
            "family_contribution": 9119,
            "need_based_score": 14,
            "applicant_sid": "89338"
        },
        {
            "family_contribution": 3329,
            "need_based_score": 22,
            "applicant_sid": "89339"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -16,
            "applicant_sid": "89340"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -19,
            "applicant_sid": "89341"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -23,
            "applicant_sid": "89342"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -16,
            "applicant_sid": "89343"
        },
        {
            "family_contribution": 7171,
            "need_based_score": 14,
            "applicant_sid": "89344"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -21,
            "applicant_sid": "89345"
        },
        {
            "family_contribution": 307943,
            "need_based_score": 6,
            "applicant_sid": "89346"
        },
        {
            "family_contribution": 0,
            "need_based_score": 24,
            "applicant_sid": "89347"
        },
        {
            "family_contribution": 10846,
            "need_based_score": 14,
            "applicant_sid": "89348"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -20,
            "applicant_sid": "89349"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -21,
            "applicant_sid": "89350"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -17,
            "applicant_sid": "89351"
        },
        {
            "family_contribution": 4046,
            "need_based_score": 25,
            "applicant_sid": "89352"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -16,
            "applicant_sid": "89353"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -16,
            "applicant_sid": "89354"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -19,
            "applicant_sid": "89355"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -20,
            "applicant_sid": "89356"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -20,
            "applicant_sid": "89357"
        },
        {
            "family_contribution": 232,
            "need_based_score": 21,
            "applicant_sid": "89358"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -16,
            "applicant_sid": "89359"
        },
        {
            "family_contribution": 25374,
            "need_based_score": 13,
            "applicant_sid": "89360"
        },
        {
            "family_contribution": 2613,
            "need_based_score": 22,
            "applicant_sid": "89361"
        },
        {
            "family_contribution": 25831,
            "need_based_score": 9,
            "applicant_sid": "89362"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -18,
            "applicant_sid": "89363"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -20,
            "applicant_sid": "89364"
        },
        {
            "family_contribution": 16026,
            "need_based_score": 12,
            "applicant_sid": "89365"
        },
        {
            "family_contribution": 127452,
            "need_based_score": 7,
            "applicant_sid": "89366"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -19,
            "applicant_sid": "89367"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -21,
            "applicant_sid": "89368"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -21,
            "applicant_sid": "89369"
        },
        {
            "family_contribution": 25813,
            "need_based_score": 13,
            "applicant_sid": "89370"
        },
        {
            "family_contribution": 0,
            "need_based_score": 25,
            "applicant_sid": "89371"
        },
        {
            "family_contribution": 0,
            "need_based_score": 25,
            "applicant_sid": "89372"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -20,
            "applicant_sid": "89373"
        },
        {
            "family_contribution": 2520,
            "need_based_score": 24,
            "applicant_sid": "89374"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -16,
            "applicant_sid": "89375"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -19,
            "applicant_sid": "89376"
        },
        {
            "family_contribution": 49048,
            "need_based_score": 11,
            "applicant_sid": "89377"
        },
        {
            "family_contribution": 0,
            "need_based_score": 25,
            "applicant_sid": "89378"
        },
        {
            "family_contribution": 5222,
            "need_based_score": 17,
            "applicant_sid": "89379"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -16,
            "applicant_sid": "89380"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -17,
            "applicant_sid": "89381"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -20,
            "applicant_sid": "89382"
        },
        {
            "family_contribution": 7463,
            "need_based_score": 17,
            "applicant_sid": "89383"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -16,
            "applicant_sid": "89384"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -21,
            "applicant_sid": "89385"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -16,
            "applicant_sid": "89386"
        },
        {
            "family_contribution": 14358,
            "need_based_score": 13,
            "applicant_sid": "89387"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -19,
            "applicant_sid": "89388"
        },
        {
            "family_contribution": 413,
            "need_based_score": 25,
            "applicant_sid": "89389"
        },
        {
            "family_contribution": 0,
            "need_based_score": 24,
            "applicant_sid": "89390"
        },
        {
            "family_contribution": 0,
            "need_based_score": 25,
            "applicant_sid": "89391"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -16,
            "applicant_sid": "89392"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -16,
            "applicant_sid": "89393"
        },
        {
            "family_contribution": 0,
            "need_based_score": 22,
            "applicant_sid": "89394"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -16,
            "applicant_sid": "89395"
        },
        {
            "family_contribution": 0,
            "need_based_score": 22,
            "applicant_sid": "89396"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -19,
            "applicant_sid": "89397"
        },
        {
            "family_contribution": 14834,
            "need_based_score": 14,
            "applicant_sid": "89398"
        },
        {
            "family_contribution": 0,
            "need_based_score": 25,
            "applicant_sid": "89399"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -16,
            "applicant_sid": "89400"
        },
        {
            "family_contribution": 2615,
            "need_based_score": 25,
            "applicant_sid": "89401"
        },
        {
            "family_contribution": 934,
            "need_based_score": 25,
            "applicant_sid": "89402"
        },
        {
            "family_contribution": 0,
            "need_based_score": 21,
            "applicant_sid": "89403"
        },
        {
            "family_contribution": 4511,
            "need_based_score": 25,
            "applicant_sid": "89404"
        },
        {
            "family_contribution": 9919,
            "need_based_score": 12,
            "applicant_sid": "89405"
        },
        {
            "family_contribution": 0,
            "need_based_score": 22,
            "applicant_sid": "89406"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -19,
            "applicant_sid": "89407"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -20,
            "applicant_sid": "89408"
        },
        {
            "family_contribution": 89207,
            "need_based_score": 7,
            "applicant_sid": "89409"
        },
        {
            "family_contribution": 0,
            "need_based_score": 22,
            "applicant_sid": "89410"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -16,
            "applicant_sid": "89411"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -20,
            "applicant_sid": "89412"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -23,
            "applicant_sid": "89413"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -24,
            "applicant_sid": "89414"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -22,
            "applicant_sid": "89415"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -16,
            "applicant_sid": "89416"
        },
        {
            "family_contribution": 31939,
            "need_based_score": 9,
            "applicant_sid": "89417"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -19,
            "applicant_sid": "89418"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -17,
            "applicant_sid": "89419"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -19,
            "applicant_sid": "89420"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -19,
            "applicant_sid": "89421"
        },
        {
            "family_contribution": 50314,
            "need_based_score": 10,
            "applicant_sid": "89422"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -20,
            "applicant_sid": "89423"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -22,
            "applicant_sid": "89424"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -19,
            "applicant_sid": "89425"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -23,
            "applicant_sid": "89426"
        },
        {
            "family_contribution": 3354,
            "need_based_score": 21,
            "applicant_sid": "89427"
        },
        {
            "family_contribution": 0,
            "need_based_score": 25,
            "applicant_sid": "89428"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -19,
            "applicant_sid": "89429"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -21,
            "applicant_sid": "89430"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -24,
            "applicant_sid": "89431"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -19,
            "applicant_sid": "89432"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -19,
            "applicant_sid": "89433"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -22,
            "applicant_sid": "89434"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -16,
            "applicant_sid": "89435"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -20,
            "applicant_sid": "89436"
        },
        {
            "family_contribution": 9034,
            "need_based_score": 17,
            "applicant_sid": "89437"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -19,
            "applicant_sid": "89438"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -19,
            "applicant_sid": "89439"
        },
        {
            "family_contribution": 0,
            "need_based_score": 21,
            "applicant_sid": "89440"
        },
        {
            "family_contribution": 53609,
            "need_based_score": 7,
            "applicant_sid": "89441"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -19,
            "applicant_sid": "89442"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -19,
            "applicant_sid": "89443"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -19,
            "applicant_sid": "89444"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -19,
            "applicant_sid": "89445"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -19,
            "applicant_sid": "89446"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -16,
            "applicant_sid": "89447"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -17,
            "applicant_sid": "89448"
        },
        {
            "family_contribution": 78464,
            "need_based_score": 10,
            "applicant_sid": "89449"
        },
        {
            "family_contribution": 0,
            "need_based_score": 22,
            "applicant_sid": "89450"
        },
        {
            "family_contribution": 0,
            "need_based_score": 23,
            "applicant_sid": "89451"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -19,
            "applicant_sid": "89452"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -16,
            "applicant_sid": "89453"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -19,
            "applicant_sid": "89454"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -16,
            "applicant_sid": "89455"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -19,
            "applicant_sid": "89456"
        },
        {
            "family_contribution": 17570,
            "need_based_score": 10,
            "applicant_sid": "89457"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -19,
            "applicant_sid": "89458"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -23,
            "applicant_sid": "89459"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -19,
            "applicant_sid": "89460"
        },
        {
            "family_contribution": 49148,
            "need_based_score": 8,
            "applicant_sid": "89461"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -22,
            "applicant_sid": "89462"
        },
        {
            "family_contribution": 5113,
            "need_based_score": 13,
            "applicant_sid": "89463"
        },
        {
            "family_contribution": 4235,
            "need_based_score": 25,
            "applicant_sid": "89464"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -19,
            "applicant_sid": "89465"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -19,
            "applicant_sid": "89466"
        },
        {
            "family_contribution": 124876,
            "need_based_score": 7,
            "applicant_sid": "89467"
        },
        {
            "family_contribution": 29635,
            "need_based_score": 8,
            "applicant_sid": "89468"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -19,
            "applicant_sid": "89469"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -19,
            "applicant_sid": "89470"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -22,
            "applicant_sid": "89471"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -17,
            "applicant_sid": "89472"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -16,
            "applicant_sid": "89473"
        },
        {
            "family_contribution": 0,
            "need_based_score": 24,
            "applicant_sid": "89474"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -16,
            "applicant_sid": "89475"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -18,
            "applicant_sid": "89476"
        },
        {
            "family_contribution": 3282,
            "need_based_score": 22,
            "applicant_sid": "89477"
        },
        {
            "family_contribution": 7433,
            "need_based_score": 17,
            "applicant_sid": "89478"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -22,
            "applicant_sid": "89479"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -16,
            "applicant_sid": "89480"
        },
        {
            "family_contribution": 3684,
            "need_based_score": 20,
            "applicant_sid": "89481"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -18,
            "applicant_sid": "89482"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -22,
            "applicant_sid": "89483"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -22,
            "applicant_sid": "89484"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -19,
            "applicant_sid": "89485"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -22,
            "applicant_sid": "89486"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -21,
            "applicant_sid": "89487"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -22,
            "applicant_sid": "89488"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -19,
            "applicant_sid": "89489"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -16,
            "applicant_sid": "89490"
        },
        {
            "family_contribution": 1876889,
            "need_based_score": 7,
            "applicant_sid": "89491"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -22,
            "applicant_sid": "89492"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -16,
            "applicant_sid": "89493"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -20,
            "applicant_sid": "89494"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -16,
            "applicant_sid": "89495"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -22,
            "applicant_sid": "89496"
        },
        {
            "family_contribution": 0,
            "need_based_score": 22,
            "applicant_sid": "89497"
        },
        {
            "family_contribution": 27753,
            "need_based_score": 9,
            "applicant_sid": "89498"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -16,
            "applicant_sid": "89499"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -19,
            "applicant_sid": "89500"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -22,
            "applicant_sid": "89501"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -20,
            "applicant_sid": "89502"
        },
        {
            "family_contribution": 0,
            "need_based_score": 22,
            "applicant_sid": "89503"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -23,
            "applicant_sid": "89504"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -19,
            "applicant_sid": "89505"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -19,
            "applicant_sid": "89506"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -20,
            "applicant_sid": "89507"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -19,
            "applicant_sid": "89508"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -16,
            "applicant_sid": "89509"
        },
        {
            "family_contribution": 192690,
            "need_based_score": 9,
            "applicant_sid": "89510"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -16,
            "applicant_sid": "89511"
        },
        {
            "family_contribution": 11203,
            "need_based_score": 13,
            "applicant_sid": "89512"
        },
        {
            "family_contribution": 0,
            "need_based_score": 24,
            "applicant_sid": "89513"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -19,
            "applicant_sid": "89514"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -23,
            "applicant_sid": "89515"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -20,
            "applicant_sid": "89516"
        },
        {
            "family_contribution": 1276,
            "need_based_score": 20,
            "applicant_sid": "89517"
        },
        {
            "family_contribution": 821,
            "need_based_score": 25,
            "applicant_sid": "89518"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -21,
            "applicant_sid": "89519"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -16,
            "applicant_sid": "89520"
        },
        {
            "family_contribution": 1508,
            "need_based_score": 25,
            "applicant_sid": "89521"
        },
        {
            "family_contribution": 3834,
            "need_based_score": 22,
            "applicant_sid": "89522"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -20,
            "applicant_sid": "89523"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -19,
            "applicant_sid": "89524"
        },
        {
            "family_contribution": 4575,
            "need_based_score": 22,
            "applicant_sid": "89525"
        },
        {
            "family_contribution": 56774,
            "need_based_score": 6,
            "applicant_sid": "89526"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -17,
            "applicant_sid": "89527"
        },
        {
            "family_contribution": 18627,
            "need_based_score": 10,
            "applicant_sid": "89528"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -21,
            "applicant_sid": "89529"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -19,
            "applicant_sid": "89530"
        },
        {
            "family_contribution": 0,
            "need_based_score": 21,
            "applicant_sid": "89531"
        },
        {
            "family_contribution": 4104,
            "need_based_score": 25,
            "applicant_sid": "89532"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -23,
            "applicant_sid": "89533"
        },
        {
            "family_contribution": 202558,
            "need_based_score": 10,
            "applicant_sid": "89534"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -19,
            "applicant_sid": "89535"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -16,
            "applicant_sid": "89536"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -19,
            "applicant_sid": "89537"
        },
        {
            "family_contribution": 23809,
            "need_based_score": 10,
            "applicant_sid": "89538"
        },
        {
            "family_contribution": 57987,
            "need_based_score": 7,
            "applicant_sid": "89539"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -22,
            "applicant_sid": "89540"
        },
        {
            "family_contribution": 400835,
            "need_based_score": 10,
            "applicant_sid": "89541"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -19,
            "applicant_sid": "89542"
        },
        {
            "family_contribution": 11517,
            "need_based_score": 13,
            "applicant_sid": "89543"
        },
        {
            "family_contribution": 0,
            "need_based_score": 22,
            "applicant_sid": "89544"
        },
        {
            "family_contribution": 0,
            "need_based_score": 25,
            "applicant_sid": "89545"
        },
        {
            "family_contribution": 1383,
            "need_based_score": 25,
            "applicant_sid": "89546"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -23,
            "applicant_sid": "89547"
        },
        {
            "family_contribution": 24203,
            "need_based_score": 9,
            "applicant_sid": "89548"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -20,
            "applicant_sid": "89549"
        },
        {
            "family_contribution": 4038,
            "need_based_score": 25,
            "applicant_sid": "89550"
        },
        {
            "family_contribution": 15028,
            "need_based_score": 8,
            "applicant_sid": "89551"
        },
        {
            "family_contribution": 14097,
            "need_based_score": 13,
            "applicant_sid": "89552"
        },
        {
            "family_contribution": 5031,
            "need_based_score": 17,
            "applicant_sid": "89553"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -19,
            "applicant_sid": "89554"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -16,
            "applicant_sid": "89555"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -17,
            "applicant_sid": "89556"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -23,
            "applicant_sid": "89557"
        },
        {
            "family_contribution": 0,
            "need_based_score": 25,
            "applicant_sid": "89558"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -16,
            "applicant_sid": "89559"
        },
        {
            "family_contribution": 227713,
            "need_based_score": 6,
            "applicant_sid": "89560"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -19,
            "applicant_sid": "89561"
        },
        {
            "family_contribution": 4084,
            "need_based_score": 25,
            "applicant_sid": "89562"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -20,
            "applicant_sid": "89563"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -20,
            "applicant_sid": "89564"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -20,
            "applicant_sid": "89565"
        },
        {
            "family_contribution": 0,
            "need_based_score": 6,
            "applicant_sid": "89566"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -20,
            "applicant_sid": "89567"
        },
        {
            "family_contribution": 67085,
            "need_based_score": 5,
            "applicant_sid": "89568"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -22,
            "applicant_sid": "89569"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -24,
            "applicant_sid": "89570"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -19,
            "applicant_sid": "89571"
        },
        {
            "family_contribution": 25292,
            "need_based_score": 8,
            "applicant_sid": "89572"
        },
        {
            "family_contribution": 36722,
            "need_based_score": 7,
            "applicant_sid": "89573"
        },
        {
            "family_contribution": 0,
            "need_based_score": 21,
            "applicant_sid": "89574"
        },
        {
            "family_contribution": 18827,
            "need_based_score": 9,
            "applicant_sid": "89575"
        },
        {
            "family_contribution": 0,
            "need_based_score": 26,
            "applicant_sid": "89576"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -19,
            "applicant_sid": "89577"
        },
        {
            "family_contribution": 36770,
            "need_based_score": 6,
            "applicant_sid": "89578"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -21,
            "applicant_sid": "89579"
        },
        {
            "family_contribution": 7956,
            "need_based_score": 12,
            "applicant_sid": "89580"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -19,
            "applicant_sid": "89581"
        },
        {
            "family_contribution": 1721,
            "need_based_score": 21,
            "applicant_sid": "89582"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -16,
            "applicant_sid": "89583"
        },
        {
            "family_contribution": 69455,
            "need_based_score": 7,
            "applicant_sid": "89584"
        },
        {
            "family_contribution": 0,
            "need_based_score": 21,
            "applicant_sid": "89585"
        },
        {
            "family_contribution": 7525,
            "need_based_score": 14,
            "applicant_sid": "89586"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -23,
            "applicant_sid": "89587"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -20,
            "applicant_sid": "89588"
        },
        {
            "family_contribution": 201050,
            "need_based_score": 6,
            "applicant_sid": "89589"
        },
        {
            "family_contribution": 0,
            "need_based_score": 25,
            "applicant_sid": "89590"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -22,
            "applicant_sid": "89591"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -22,
            "applicant_sid": "89592"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -19,
            "applicant_sid": "89593"
        },
        {
            "family_contribution": 28877,
            "need_based_score": 8,
            "applicant_sid": "89594"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -22,
            "applicant_sid": "89595"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -19,
            "applicant_sid": "89596"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -20,
            "applicant_sid": "89597"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -23,
            "applicant_sid": "89598"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -23,
            "applicant_sid": "89599"
        },
        {
            "family_contribution": 0,
            "need_based_score": 25,
            "applicant_sid": "89600"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -19,
            "applicant_sid": "89601"
        },
        {
            "family_contribution": 2475,
            "need_based_score": 22,
            "applicant_sid": "89602"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -19,
            "applicant_sid": "89603"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -22,
            "applicant_sid": "89604"
        },
        {
            "family_contribution": 162404,
            "need_based_score": 5,
            "applicant_sid": "89605"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -19,
            "applicant_sid": "89606"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -19,
            "applicant_sid": "89607"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -22,
            "applicant_sid": "89608"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -19,
            "applicant_sid": "89609"
        },
        {
            "family_contribution": 40510,
            "need_based_score": 11,
            "applicant_sid": "89610"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -16,
            "applicant_sid": "89611"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -19,
            "applicant_sid": "89612"
        },
        {
            "family_contribution": 0,
            "need_based_score": 21,
            "applicant_sid": "89613"
        },
        {
            "family_contribution": 3115,
            "need_based_score": 25,
            "applicant_sid": "89614"
        },
        {
            "family_contribution": 2861,
            "need_based_score": 22,
            "applicant_sid": "89615"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -22,
            "applicant_sid": "89616"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -22,
            "applicant_sid": "89617"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -16,
            "applicant_sid": "89618"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -16,
            "applicant_sid": "89619"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -16,
            "applicant_sid": "89620"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -23,
            "applicant_sid": "89621"
        },
        {
            "family_contribution": 0,
            "need_based_score": 20,
            "applicant_sid": "89622"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -23,
            "applicant_sid": "89623"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -22,
            "applicant_sid": "89624"
        },
        {
            "family_contribution": 302941,
            "need_based_score": 7,
            "applicant_sid": "89625"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -19,
            "applicant_sid": "89626"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -19,
            "applicant_sid": "89627"
        },
        {
            "family_contribution": 1484,
            "need_based_score": 21,
            "applicant_sid": "89628"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -16,
            "applicant_sid": "89629"
        },
        {
            "family_contribution": 9175,
            "need_based_score": 14,
            "applicant_sid": "89630"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -19,
            "applicant_sid": "89631"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -23,
            "applicant_sid": "89632"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -22,
            "applicant_sid": "89633"
        },
        {
            "family_contribution": 0,
            "need_based_score": 22,
            "applicant_sid": "89634"
        },
        {
            "family_contribution": 28274,
            "need_based_score": 9,
            "applicant_sid": "89635"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -24,
            "applicant_sid": "89636"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -19,
            "applicant_sid": "89637"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -16,
            "applicant_sid": "89638"
        },
        {
            "family_contribution": 60103,
            "need_based_score": 6,
            "applicant_sid": "89639"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -24,
            "applicant_sid": "89640"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -19,
            "applicant_sid": "89641"
        },
        {
            "family_contribution": 246,
            "need_based_score": 25,
            "applicant_sid": "89642"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -19,
            "applicant_sid": "89643"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -19,
            "applicant_sid": "89644"
        },
        {
            "family_contribution": 62724,
            "need_based_score": 6,
            "applicant_sid": "89645"
        },
        {
            "family_contribution": 0,
            "need_based_score": 25,
            "applicant_sid": "89646"
        },
        {
            "family_contribution": 13234,
            "need_based_score": 13,
            "applicant_sid": "89647"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -19,
            "applicant_sid": "89648"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -22,
            "applicant_sid": "89649"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -19,
            "applicant_sid": "89650"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -19,
            "applicant_sid": "89651"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -19,
            "applicant_sid": "89652"
        },
        {
            "family_contribution": 379,
            "need_based_score": 21,
            "applicant_sid": "89653"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -16,
            "applicant_sid": "89654"
        },
        {
            "family_contribution": 39688,
            "need_based_score": 8,
            "applicant_sid": "89655"
        },
        {
            "family_contribution": 2316,
            "need_based_score": 25,
            "applicant_sid": "89656"
        },
        {
            "family_contribution": 14638,
            "need_based_score": 17,
            "applicant_sid": "89657"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -16,
            "applicant_sid": "89658"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -16,
            "applicant_sid": "89659"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -19,
            "applicant_sid": "89660"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -19,
            "applicant_sid": "89661"
        },
        {
            "family_contribution": 28911,
            "need_based_score": 13,
            "applicant_sid": "89662"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -19,
            "applicant_sid": "89663"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -22,
            "applicant_sid": "89664"
        },
        {
            "family_contribution": 1085,
            "need_based_score": 22,
            "applicant_sid": "89665"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -19,
            "applicant_sid": "89666"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -19,
            "applicant_sid": "89667"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -19,
            "applicant_sid": "89668"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -22,
            "applicant_sid": "89669"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -20,
            "applicant_sid": "89670"
        },
        {
            "family_contribution": 1334,
            "need_based_score": 25,
            "applicant_sid": "89671"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -19,
            "applicant_sid": "89672"
        },
        {
            "family_contribution": 0,
            "need_based_score": 25,
            "applicant_sid": "89673"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -19,
            "applicant_sid": "89674"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -16,
            "applicant_sid": "89675"
        },
        {
            "family_contribution": 6173,
            "need_based_score": 17,
            "applicant_sid": "89676"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -22,
            "applicant_sid": "89677"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -19,
            "applicant_sid": "89678"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -21,
            "applicant_sid": "89679"
        },
        {
            "family_contribution": 29659,
            "need_based_score": 13,
            "applicant_sid": "89680"
        },
        {
            "family_contribution": 82476,
            "need_based_score": 7,
            "applicant_sid": "89681"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -22,
            "applicant_sid": "89682"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -16,
            "applicant_sid": "89683"
        },
        {
            "family_contribution": 418160,
            "need_based_score": 6,
            "applicant_sid": "89684"
        },
        {
            "family_contribution": 25789,
            "need_based_score": 13,
            "applicant_sid": "89685"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -15,
            "applicant_sid": "89686"
        },
        {
            "family_contribution": 3622,
            "need_based_score": 25,
            "applicant_sid": "89687"
        },
        {
            "family_contribution": 8844,
            "need_based_score": 14,
            "applicant_sid": "89688"
        },
        {
            "family_contribution": 0,
            "need_based_score": 25,
            "applicant_sid": "89689"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -19,
            "applicant_sid": "89690"
        },
        {
            "family_contribution": 4892,
            "need_based_score": 20,
            "applicant_sid": "89691"
        },
        {
            "family_contribution": 3194,
            "need_based_score": 20,
            "applicant_sid": "89692"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -19,
            "applicant_sid": "89693"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -19,
            "applicant_sid": "89694"
        },
        {
            "family_contribution": 4726,
            "need_based_score": 22,
            "applicant_sid": "89695"
        },
        {
            "family_contribution": 18438,
            "need_based_score": 13,
            "applicant_sid": "89696"
        },
        {
            "family_contribution": 29489,
            "need_based_score": 10,
            "applicant_sid": "89697"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -21,
            "applicant_sid": "89698"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -19,
            "applicant_sid": "89699"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -19,
            "applicant_sid": "89700"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -16,
            "applicant_sid": "89701"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -16,
            "applicant_sid": "89702"
        },
        {
            "family_contribution": 24733,
            "need_based_score": 10,
            "applicant_sid": "89703"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -21,
            "applicant_sid": "89704"
        },
        {
            "family_contribution": 993,
            "need_based_score": 26,
            "applicant_sid": "89705"
        },
        {
            "family_contribution": 0,
            "need_based_score": 22,
            "applicant_sid": "89706"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -22,
            "applicant_sid": "89707"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -19,
            "applicant_sid": "89708"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -19,
            "applicant_sid": "89709"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -22,
            "applicant_sid": "89710"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -19,
            "applicant_sid": "89711"
        },
        {
            "family_contribution": 5315,
            "need_based_score": 14,
            "applicant_sid": "89712"
        },
        {
            "family_contribution": 11269,
            "need_based_score": 12,
            "applicant_sid": "89713"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -16,
            "applicant_sid": "89714"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -22,
            "applicant_sid": "89715"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -16,
            "applicant_sid": "89716"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -16,
            "applicant_sid": "89717"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -22,
            "applicant_sid": "89718"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -22,
            "applicant_sid": "89719"
        },
        {
            "family_contribution": 38740,
            "need_based_score": 7,
            "applicant_sid": "89720"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -19,
            "applicant_sid": "89721"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -19,
            "applicant_sid": "89722"
        },
        {
            "family_contribution": 2130,
            "need_based_score": 21,
            "applicant_sid": "89723"
        },
        {
            "family_contribution": 17789,
            "need_based_score": 10,
            "applicant_sid": "89724"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -16,
            "applicant_sid": "89725"
        },
        {
            "family_contribution": 8173,
            "need_based_score": 17,
            "applicant_sid": "89726"
        },
        {
            "family_contribution": 17941,
            "need_based_score": 8,
            "applicant_sid": "89727"
        },
        {
            "family_contribution": 1137,
            "need_based_score": 25,
            "applicant_sid": "89728"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -20,
            "applicant_sid": "89729"
        },
        {
            "family_contribution": 3850,
            "need_based_score": 25,
            "applicant_sid": "89730"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -19,
            "applicant_sid": "89731"
        },
        {
            "family_contribution": 0,
            "need_based_score": 22,
            "applicant_sid": "89732"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -19,
            "applicant_sid": "89733"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -16,
            "applicant_sid": "89734"
        },
        {
            "family_contribution": 0,
            "need_based_score": 22,
            "applicant_sid": "89735"
        },
        {
            "family_contribution": 7360,
            "need_based_score": 14,
            "applicant_sid": "89736"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -22,
            "applicant_sid": "89737"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -19,
            "applicant_sid": "89738"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -19,
            "applicant_sid": "89739"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -19,
            "applicant_sid": "89740"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -16,
            "applicant_sid": "89741"
        },
        {
            "family_contribution": 31059,
            "need_based_score": 10,
            "applicant_sid": "89742"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -17,
            "applicant_sid": "89743"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -18,
            "applicant_sid": "89744"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -16,
            "applicant_sid": "89745"
        },
        {
            "family_contribution": 6419,
            "need_based_score": 14,
            "applicant_sid": "89746"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -22,
            "applicant_sid": "89747"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -19,
            "applicant_sid": "89748"
        },
        {
            "family_contribution": 12648,
            "need_based_score": 13,
            "applicant_sid": "89749"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -21,
            "applicant_sid": "89750"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -15,
            "applicant_sid": "89751"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -24,
            "applicant_sid": "89752"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -22,
            "applicant_sid": "89753"
        },
        {
            "family_contribution": 1436,
            "need_based_score": 22,
            "applicant_sid": "89754"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -16,
            "applicant_sid": "89755"
        },
        {
            "family_contribution": 63504,
            "need_based_score": 10,
            "applicant_sid": "89756"
        },
        {
            "family_contribution": 2165,
            "need_based_score": 22,
            "applicant_sid": "89757"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -19,
            "applicant_sid": "89758"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -16,
            "applicant_sid": "89759"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -19,
            "applicant_sid": "89760"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -19,
            "applicant_sid": "89761"
        },
        {
            "family_contribution": 26975,
            "need_based_score": 13,
            "applicant_sid": "89762"
        },
        {
            "family_contribution": 0,
            "need_based_score": 25,
            "applicant_sid": "89763"
        },
        {
            "family_contribution": 14886,
            "need_based_score": 14,
            "applicant_sid": "89764"
        },
        {
            "family_contribution": 2701,
            "need_based_score": 25,
            "applicant_sid": "89765"
        },
        {
            "family_contribution": 25891,
            "need_based_score": 10,
            "applicant_sid": "89766"
        },
        {
            "family_contribution": 0,
            "need_based_score": 25,
            "applicant_sid": "89767"
        },
        {
            "family_contribution": 66708,
            "need_based_score": 6,
            "applicant_sid": "89768"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -20,
            "applicant_sid": "89769"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -19,
            "applicant_sid": "89770"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -16,
            "applicant_sid": "89771"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -17,
            "applicant_sid": "89772"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -22,
            "applicant_sid": "89773"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -16,
            "applicant_sid": "89774"
        },
        {
            "family_contribution": 67242,
            "need_based_score": 5,
            "applicant_sid": "89775"
        },
        {
            "family_contribution": 3885,
            "need_based_score": 25,
            "applicant_sid": "89776"
        },
        {
            "family_contribution": 0,
            "need_based_score": 25,
            "applicant_sid": "89777"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -19,
            "applicant_sid": "89778"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -22,
            "applicant_sid": "89779"
        },
        {
            "family_contribution": 12412,
            "need_based_score": 13,
            "applicant_sid": "89780"
        },
        {
            "family_contribution": 49075,
            "need_based_score": 6,
            "applicant_sid": "89781"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -23,
            "applicant_sid": "89782"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -22,
            "applicant_sid": "89783"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -19,
            "applicant_sid": "89784"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -19,
            "applicant_sid": "89785"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -22,
            "applicant_sid": "89786"
        },
        {
            "family_contribution": 0,
            "need_based_score": 25,
            "applicant_sid": "89787"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -18,
            "applicant_sid": "89788"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -19,
            "applicant_sid": "89789"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -20,
            "applicant_sid": "89790"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -22,
            "applicant_sid": "89791"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -19,
            "applicant_sid": "89792"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -22,
            "applicant_sid": "89793"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -24,
            "applicant_sid": "89794"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -22,
            "applicant_sid": "89795"
        },
        {
            "family_contribution": 3643,
            "need_based_score": 21,
            "applicant_sid": "89796"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -16,
            "applicant_sid": "89797"
        },
        {
            "family_contribution": 12952,
            "need_based_score": 12,
            "applicant_sid": "89798"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -22,
            "applicant_sid": "89799"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -19,
            "applicant_sid": "89800"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -16,
            "applicant_sid": "89801"
        },
        {
            "family_contribution": 179533,
            "need_based_score": 12,
            "applicant_sid": "89802"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -22,
            "applicant_sid": "89803"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -20,
            "applicant_sid": "89804"
        },
        {
            "family_contribution": 8585,
            "need_based_score": 13,
            "applicant_sid": "89805"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -19,
            "applicant_sid": "89806"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -21,
            "applicant_sid": "89807"
        },
        {
            "family_contribution": 4632,
            "need_based_score": 20,
            "applicant_sid": "89808"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -20,
            "applicant_sid": "89809"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -19,
            "applicant_sid": "89810"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -19,
            "applicant_sid": "89811"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -22,
            "applicant_sid": "89812"
        },
        {
            "family_contribution": 0,
            "need_based_score": 22,
            "applicant_sid": "89813"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -19,
            "applicant_sid": "89814"
        },
        {
            "family_contribution": 250,
            "need_based_score": 21,
            "applicant_sid": "89815"
        },
        {
            "family_contribution": 0,
            "need_based_score": 22,
            "applicant_sid": "89816"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -19,
            "applicant_sid": "89817"
        },
        {
            "family_contribution": 0,
            "need_based_score": 26,
            "applicant_sid": "89818"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -16,
            "applicant_sid": "89819"
        },
        {
            "family_contribution": 0,
            "need_based_score": 22,
            "applicant_sid": "89820"
        },
        {
            "family_contribution": 1409,
            "need_based_score": 25,
            "applicant_sid": "89821"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -19,
            "applicant_sid": "89822"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -19,
            "applicant_sid": "89823"
        },
        {
            "family_contribution": 0,
            "need_based_score": 21,
            "applicant_sid": "89824"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -20,
            "applicant_sid": "89825"
        },
        {
            "family_contribution": 1034,
            "need_based_score": 25,
            "applicant_sid": "89826"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -19,
            "applicant_sid": "89827"
        },
        {
            "family_contribution": 4370,
            "need_based_score": 24,
            "applicant_sid": "89828"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -20,
            "applicant_sid": "89829"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -23,
            "applicant_sid": "89830"
        },
        {
            "family_contribution": 0,
            "need_based_score": 21,
            "applicant_sid": "89831"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -19,
            "applicant_sid": "89832"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -19,
            "applicant_sid": "89833"
        },
        {
            "family_contribution": 0,
            "need_based_score": 22,
            "applicant_sid": "89834"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -19,
            "applicant_sid": "89835"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -17,
            "applicant_sid": "89836"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -16,
            "applicant_sid": "89837"
        },
        {
            "family_contribution": 24685,
            "need_based_score": 8,
            "applicant_sid": "89838"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -18,
            "applicant_sid": "89839"
        },
        {
            "family_contribution": 15201,
            "need_based_score": 9,
            "applicant_sid": "89840"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -19,
            "applicant_sid": "89841"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -18,
            "applicant_sid": "89842"
        },
        {
            "family_contribution": 21747,
            "need_based_score": 9,
            "applicant_sid": "89843"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -19,
            "applicant_sid": "89844"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -24,
            "applicant_sid": "89845"
        },
        {
            "family_contribution": 4034,
            "need_based_score": 21,
            "applicant_sid": "89846"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -19,
            "applicant_sid": "89847"
        },
        {
            "family_contribution": 3177,
            "need_based_score": 20,
            "applicant_sid": "89848"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -20,
            "applicant_sid": "89849"
        },
        {
            "family_contribution": 168568,
            "need_based_score": 7,
            "applicant_sid": "89850"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -19,
            "applicant_sid": "89851"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -19,
            "applicant_sid": "89852"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -19,
            "applicant_sid": "89853"
        },
        {
            "family_contribution": 4185,
            "need_based_score": 22,
            "applicant_sid": "89854"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -19,
            "applicant_sid": "89855"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -19,
            "applicant_sid": "89856"
        },
        {
            "family_contribution": 35125,
            "need_based_score": 7,
            "applicant_sid": "89857"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -16,
            "applicant_sid": "89858"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -18,
            "applicant_sid": "89859"
        },
        {
            "family_contribution": 0,
            "need_based_score": 22,
            "applicant_sid": "89860"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -24,
            "applicant_sid": "89861"
        },
        {
            "family_contribution": 16941,
            "need_based_score": 9,
            "applicant_sid": "89862"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -23,
            "applicant_sid": "89863"
        },
        {
            "family_contribution": 0,
            "need_based_score": 25,
            "applicant_sid": "89864"
        },
        {
            "family_contribution": 21067,
            "need_based_score": 9,
            "applicant_sid": "89865"
        },
        {
            "family_contribution": 0,
            "need_based_score": 22,
            "applicant_sid": "89866"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -16,
            "applicant_sid": "89867"
        },
        {
            "family_contribution": 0,
            "need_based_score": 25,
            "applicant_sid": "89868"
        },
        {
            "family_contribution": 0,
            "need_based_score": 22,
            "applicant_sid": "89869"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -23,
            "applicant_sid": "89870"
        },
        {
            "family_contribution": 18521,
            "need_based_score": 9,
            "applicant_sid": "89871"
        },
        {
            "family_contribution": 63399,
            "need_based_score": 6,
            "applicant_sid": "89872"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -16,
            "applicant_sid": "89873"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -19,
            "applicant_sid": "89874"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -20,
            "applicant_sid": "89875"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -19,
            "applicant_sid": "89876"
        },
        {
            "family_contribution": 12363,
            "need_based_score": 12,
            "applicant_sid": "89877"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -23,
            "applicant_sid": "89878"
        },
        {
            "family_contribution": 603,
            "need_based_score": 25,
            "applicant_sid": "89879"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -16,
            "applicant_sid": "89880"
        },
        {
            "family_contribution": 0,
            "need_based_score": 25,
            "applicant_sid": "89881"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -20,
            "applicant_sid": "89882"
        },
        {
            "family_contribution": 4189,
            "need_based_score": 25,
            "applicant_sid": "89883"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -23,
            "applicant_sid": "89884"
        },
        {
            "family_contribution": 0,
            "need_based_score": 21,
            "applicant_sid": "89885"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -22,
            "applicant_sid": "89886"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -24,
            "applicant_sid": "89887"
        },
        {
            "family_contribution": 5447,
            "need_based_score": 12,
            "applicant_sid": "89888"
        },
        {
            "family_contribution": 40603,
            "need_based_score": 7,
            "applicant_sid": "89889"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -19,
            "applicant_sid": "89890"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -22,
            "applicant_sid": "89891"
        },
        {
            "family_contribution": 739,
            "need_based_score": 21,
            "applicant_sid": "89892"
        },
        {
            "family_contribution": 764,
            "need_based_score": 25,
            "applicant_sid": "89893"
        },
        {
            "family_contribution": 56125,
            "need_based_score": 6,
            "applicant_sid": "89894"
        },
        {
            "family_contribution": 48829,
            "need_based_score": 8,
            "applicant_sid": "89895"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -19,
            "applicant_sid": "89896"
        },
        {
            "family_contribution": 0,
            "need_based_score": 26,
            "applicant_sid": "89897"
        },
        {
            "family_contribution": 19615,
            "need_based_score": 10,
            "applicant_sid": "89898"
        },
        {
            "family_contribution": 18542,
            "need_based_score": 13,
            "applicant_sid": "89899"
        },
        {
            "family_contribution": 16537,
            "need_based_score": 9,
            "applicant_sid": "89900"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -16,
            "applicant_sid": "89901"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -19,
            "applicant_sid": "89902"
        },
        {
            "family_contribution": 52365,
            "need_based_score": 7,
            "applicant_sid": "89903"
        },
        {
            "family_contribution": 60917,
            "need_based_score": 10,
            "applicant_sid": "89904"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -19,
            "applicant_sid": "89905"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -22,
            "applicant_sid": "89906"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -19,
            "applicant_sid": "89907"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -22,
            "applicant_sid": "89908"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -22,
            "applicant_sid": "89909"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -19,
            "applicant_sid": "89910"
        },
        {
            "family_contribution": 4037,
            "need_based_score": 22,
            "applicant_sid": "89911"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -19,
            "applicant_sid": "89912"
        },
        {
            "family_contribution": 0,
            "need_based_score": 25,
            "applicant_sid": "89913"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -19,
            "applicant_sid": "89914"
        },
        {
            "family_contribution": 115196,
            "need_based_score": 6,
            "applicant_sid": "89915"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -20,
            "applicant_sid": "89916"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -16,
            "applicant_sid": "89917"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -19,
            "applicant_sid": "89918"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -16,
            "applicant_sid": "89919"
        },
        {
            "family_contribution": 2243,
            "need_based_score": 25,
            "applicant_sid": "89920"
        },
        {
            "family_contribution": 2017,
            "need_based_score": 25,
            "applicant_sid": "89921"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -19,
            "applicant_sid": "89922"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -19,
            "applicant_sid": "89923"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -23,
            "applicant_sid": "89924"
        },
        {
            "family_contribution": 11695,
            "need_based_score": 14,
            "applicant_sid": "89925"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -19,
            "applicant_sid": "89926"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -19,
            "applicant_sid": "89927"
        },
        {
            "family_contribution": 0,
            "need_based_score": 25,
            "applicant_sid": "89928"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -21,
            "applicant_sid": "89929"
        },
        {
            "family_contribution": 11490,
            "need_based_score": 13,
            "applicant_sid": "89930"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -20,
            "applicant_sid": "89931"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -19,
            "applicant_sid": "89932"
        },
        {
            "family_contribution": 16522,
            "need_based_score": 9,
            "applicant_sid": "89933"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -22,
            "applicant_sid": "89934"
        },
        {
            "family_contribution": 15489,
            "need_based_score": 8,
            "applicant_sid": "89935"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -19,
            "applicant_sid": "89936"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -23,
            "applicant_sid": "89937"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -16,
            "applicant_sid": "89938"
        },
        {
            "family_contribution": 5520,
            "need_based_score": 14,
            "applicant_sid": "89939"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -22,
            "applicant_sid": "89940"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -22,
            "applicant_sid": "89941"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -19,
            "applicant_sid": "89942"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -19,
            "applicant_sid": "89943"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -20,
            "applicant_sid": "89944"
        },
        {
            "family_contribution": 0,
            "need_based_score": 25,
            "applicant_sid": "89945"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -22,
            "applicant_sid": "89946"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -22,
            "applicant_sid": "89947"
        },
        {
            "family_contribution": 304776,
            "need_based_score": 6,
            "applicant_sid": "89948"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -19,
            "applicant_sid": "89949"
        },
        {
            "family_contribution": 17938,
            "need_based_score": 8,
            "applicant_sid": "89950"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -23,
            "applicant_sid": "89951"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -21,
            "applicant_sid": "89952"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -21,
            "applicant_sid": "89953"
        },
        {
            "family_contribution": 41562,
            "need_based_score": 7,
            "applicant_sid": "89954"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -21,
            "applicant_sid": "89955"
        },
        {
            "family_contribution": 0,
            "need_based_score": 22,
            "applicant_sid": "89956"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -16,
            "applicant_sid": "89957"
        },
        {
            "family_contribution": 16567,
            "need_based_score": 10,
            "applicant_sid": "89958"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -22,
            "applicant_sid": "89959"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -19,
            "applicant_sid": "89960"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -19,
            "applicant_sid": "89961"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -19,
            "applicant_sid": "89962"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -16,
            "applicant_sid": "89963"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -23,
            "applicant_sid": "89964"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -19,
            "applicant_sid": "89965"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -20,
            "applicant_sid": "89966"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -20,
            "applicant_sid": "89967"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -19,
            "applicant_sid": "89968"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -16,
            "applicant_sid": "89969"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -19,
            "applicant_sid": "89970"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -20,
            "applicant_sid": "89971"
        },
        {
            "family_contribution": 23892,
            "need_based_score": 13,
            "applicant_sid": "89972"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -19,
            "applicant_sid": "89973"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -20,
            "applicant_sid": "89974"
        },
        {
            "family_contribution": 0,
            "need_based_score": 25,
            "applicant_sid": "89975"
        },
        {
            "family_contribution": 18668,
            "need_based_score": 9,
            "applicant_sid": "89976"
        },
        {
            "family_contribution": 34054,
            "need_based_score": 11,
            "applicant_sid": "89977"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -19,
            "applicant_sid": "89978"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -19,
            "applicant_sid": "89979"
        },
        {
            "family_contribution": 0,
            "need_based_score": 21,
            "applicant_sid": "89980"
        },
        {
            "family_contribution": 0,
            "need_based_score": 22,
            "applicant_sid": "89981"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -16,
            "applicant_sid": "89982"
        },
        {
            "family_contribution": 865,
            "need_based_score": 25,
            "applicant_sid": "89983"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -20,
            "applicant_sid": "89984"
        },
        {
            "family_contribution": 2586,
            "need_based_score": 22,
            "applicant_sid": "89985"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -19,
            "applicant_sid": "89986"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -19,
            "applicant_sid": "89987"
        },
        {
            "family_contribution": 420,
            "need_based_score": 25,
            "applicant_sid": "89988"
        },
        {
            "family_contribution": 63792,
            "need_based_score": 5,
            "applicant_sid": "89989"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -23,
            "applicant_sid": "89990"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -20,
            "applicant_sid": "89991"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -21,
            "applicant_sid": "89992"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -16,
            "applicant_sid": "89993"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -16,
            "applicant_sid": "89994"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -20,
            "applicant_sid": "89995"
        },
        {
            "family_contribution": 49159,
            "need_based_score": 6,
            "applicant_sid": "89996"
        },
        {
            "family_contribution": 364,
            "need_based_score": 21,
            "applicant_sid": "89997"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -19,
            "applicant_sid": "89998"
        },
        {
            "family_contribution": 19367,
            "need_based_score": 8,
            "applicant_sid": "89999"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -18,
            "applicant_sid": "90000"
        },
        {
            "family_contribution": 0,
            "need_based_score": 22,
            "applicant_sid": "90001"
        },
        {
            "family_contribution": 0,
            "need_based_score": 21,
            "applicant_sid": "90002"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -19,
            "applicant_sid": "90003"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -19,
            "applicant_sid": "90004"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -16,
            "applicant_sid": "90005"
        },
        {
            "family_contribution": 0,
            "need_based_score": 22,
            "applicant_sid": "90006"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -15,
            "applicant_sid": "90007"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -19,
            "applicant_sid": "90008"
        },
        {
            "family_contribution": 0,
            "need_based_score": 21,
            "applicant_sid": "90009"
        },
        {
            "family_contribution": 6750,
            "need_based_score": 14,
            "applicant_sid": "90010"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -19,
            "applicant_sid": "90011"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -20,
            "applicant_sid": "90012"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -22,
            "applicant_sid": "90013"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -23,
            "applicant_sid": "90014"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -22,
            "applicant_sid": "90015"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -21,
            "applicant_sid": "90016"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -19,
            "applicant_sid": "90017"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -19,
            "applicant_sid": "90018"
        },
        {
            "family_contribution": 0,
            "need_based_score": 25,
            "applicant_sid": "90019"
        },
        {
            "family_contribution": 6714,
            "need_based_score": 12,
            "applicant_sid": "90020"
        },
        {
            "family_contribution": 0,
            "need_based_score": 25,
            "applicant_sid": "90021"
        },
        {
            "family_contribution": 0,
            "need_based_score": 21,
            "applicant_sid": "90022"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -22,
            "applicant_sid": "90023"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -22,
            "applicant_sid": "90024"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -20,
            "applicant_sid": "90025"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -19,
            "applicant_sid": "90026"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -24,
            "applicant_sid": "90027"
        },
        {
            "family_contribution": 52913,
            "need_based_score": 5,
            "applicant_sid": "90028"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -20,
            "applicant_sid": "90029"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -20,
            "applicant_sid": "90030"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -17,
            "applicant_sid": "90031"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -22,
            "applicant_sid": "90032"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -20,
            "applicant_sid": "90033"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -25,
            "applicant_sid": "90034"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -20,
            "applicant_sid": "90035"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -16,
            "applicant_sid": "90036"
        },
        {
            "family_contribution": 0,
            "need_based_score": 22,
            "applicant_sid": "90037"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -21,
            "applicant_sid": "90038"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -22,
            "applicant_sid": "90039"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -19,
            "applicant_sid": "90040"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -21,
            "applicant_sid": "90041"
        },
        {
            "family_contribution": 8049,
            "need_based_score": 13,
            "applicant_sid": "90042"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -20,
            "applicant_sid": "90043"
        },
        {
            "family_contribution": 0,
            "need_based_score": 21,
            "applicant_sid": "90044"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -16,
            "applicant_sid": "90045"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -21,
            "applicant_sid": "90046"
        },
        {
            "family_contribution": 0,
            "need_based_score": 20,
            "applicant_sid": "90047"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -22,
            "applicant_sid": "90048"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -16,
            "applicant_sid": "90049"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -21,
            "applicant_sid": "90050"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -21,
            "applicant_sid": "90051"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -16,
            "applicant_sid": "90052"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -22,
            "applicant_sid": "90053"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -16,
            "applicant_sid": "90054"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -19,
            "applicant_sid": "90055"
        },
        {
            "family_contribution": 39459,
            "need_based_score": 5,
            "applicant_sid": "90056"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -19,
            "applicant_sid": "90057"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -24,
            "applicant_sid": "90058"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -20,
            "applicant_sid": "90059"
        },
        {
            "family_contribution": 140591,
            "need_based_score": 5,
            "applicant_sid": "90060"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -19,
            "applicant_sid": "90061"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -22,
            "applicant_sid": "90062"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -20,
            "applicant_sid": "90063"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -19,
            "applicant_sid": "90064"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -16,
            "applicant_sid": "90065"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -24,
            "applicant_sid": "90066"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -20,
            "applicant_sid": "90067"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -16,
            "applicant_sid": "90068"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -19,
            "applicant_sid": "90069"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -19,
            "applicant_sid": "90070"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -16,
            "applicant_sid": "90071"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -20,
            "applicant_sid": "90072"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -20,
            "applicant_sid": "90073"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -16,
            "applicant_sid": "90074"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -22,
            "applicant_sid": "90075"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -19,
            "applicant_sid": "90076"
        },
        {
            "family_contribution": 0,
            "need_based_score": 21,
            "applicant_sid": "90077"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -19,
            "applicant_sid": "90078"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -24,
            "applicant_sid": "90079"
        },
        {
            "family_contribution": 0,
            "need_based_score": 22,
            "applicant_sid": "90080"
        },
        {
            "family_contribution": 0,
            "need_based_score": 21,
            "applicant_sid": "90081"
        },
        {
            "family_contribution": 25396,
            "need_based_score": 9,
            "applicant_sid": "90082"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -19,
            "applicant_sid": "90083"
        },
        {
            "family_contribution": 24984,
            "need_based_score": 8,
            "applicant_sid": "90084"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -20,
            "applicant_sid": "90085"
        },
        {
            "family_contribution": 305,
            "need_based_score": 21,
            "applicant_sid": "90086"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -20,
            "applicant_sid": "90087"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -23,
            "applicant_sid": "90088"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -18,
            "applicant_sid": "90089"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -20,
            "applicant_sid": "90090"
        },
        {
            "family_contribution": 0,
            "need_based_score": 23,
            "applicant_sid": "90091"
        },
        {
            "family_contribution": 11627,
            "need_based_score": 13,
            "applicant_sid": "90092"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -22,
            "applicant_sid": "90093"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -19,
            "applicant_sid": "90094"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -16,
            "applicant_sid": "90095"
        },
        {
            "family_contribution": 61374,
            "need_based_score": 10,
            "applicant_sid": "90096"
        },
        {
            "family_contribution": 602,
            "need_based_score": 22,
            "applicant_sid": "90097"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -19,
            "applicant_sid": "90098"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -22,
            "applicant_sid": "90099"
        },
        {
            "family_contribution": 5903,
            "need_based_score": 12,
            "applicant_sid": "90100"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -19,
            "applicant_sid": "90101"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -20,
            "applicant_sid": "90102"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -19,
            "applicant_sid": "90103"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -21,
            "applicant_sid": "90104"
        },
        {
            "family_contribution": 0,
            "need_based_score": 22,
            "applicant_sid": "90105"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -19,
            "applicant_sid": "90106"
        },
        {
            "family_contribution": 28438,
            "need_based_score": 8,
            "applicant_sid": "90107"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -16,
            "applicant_sid": "90108"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -23,
            "applicant_sid": "90109"
        },
        {
            "family_contribution": 23613,
            "need_based_score": 9,
            "applicant_sid": "90110"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -20,
            "applicant_sid": "90111"
        },
        {
            "family_contribution": 0,
            "need_based_score": 22,
            "applicant_sid": "90112"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -20,
            "applicant_sid": "90113"
        },
        {
            "family_contribution": 7512,
            "need_based_score": 17,
            "applicant_sid": "90114"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -16,
            "applicant_sid": "90115"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -22,
            "applicant_sid": "90116"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -22,
            "applicant_sid": "90117"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -19,
            "applicant_sid": "90118"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -22,
            "applicant_sid": "90119"
        },
        {
            "family_contribution": 17570,
            "need_based_score": 9,
            "applicant_sid": "90120"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -20,
            "applicant_sid": "90121"
        },
        {
            "family_contribution": 2590,
            "need_based_score": 25,
            "applicant_sid": "90122"
        },
        {
            "family_contribution": 12706,
            "need_based_score": 13,
            "applicant_sid": "90123"
        },
        {
            "family_contribution": 8166,
            "need_based_score": 14,
            "applicant_sid": "90124"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -22,
            "applicant_sid": "90125"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -16,
            "applicant_sid": "90126"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -19,
            "applicant_sid": "90127"
        },
        {
            "family_contribution": 61664,
            "need_based_score": 7,
            "applicant_sid": "90128"
        },
        {
            "family_contribution": 17879,
            "need_based_score": 8,
            "applicant_sid": "90129"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -23,
            "applicant_sid": "90130"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -21,
            "applicant_sid": "90131"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -19,
            "applicant_sid": "90132"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -16,
            "applicant_sid": "90133"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -15,
            "applicant_sid": "90134"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -20,
            "applicant_sid": "90135"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -19,
            "applicant_sid": "90136"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -22,
            "applicant_sid": "90137"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -22,
            "applicant_sid": "90138"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -16,
            "applicant_sid": "90139"
        },
        {
            "family_contribution": 0,
            "need_based_score": 22,
            "applicant_sid": "90140"
        },
        {
            "family_contribution": 4263,
            "need_based_score": 21,
            "applicant_sid": "90141"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -22,
            "applicant_sid": "90142"
        },
        {
            "family_contribution": 16688,
            "need_based_score": 9,
            "applicant_sid": "90143"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -21,
            "applicant_sid": "90144"
        },
        {
            "family_contribution": 89738,
            "need_based_score": 4,
            "applicant_sid": "90145"
        },
        {
            "family_contribution": 1081,
            "need_based_score": 22,
            "applicant_sid": "90146"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -19,
            "applicant_sid": "90147"
        },
        {
            "family_contribution": 3023,
            "need_based_score": 20,
            "applicant_sid": "90148"
        },
        {
            "family_contribution": 7500,
            "need_based_score": 13,
            "applicant_sid": "90149"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -18,
            "applicant_sid": "90150"
        },
        {
            "family_contribution": 0,
            "need_based_score": 22,
            "applicant_sid": "90151"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -19,
            "applicant_sid": "90152"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -22,
            "applicant_sid": "90153"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -24,
            "applicant_sid": "90154"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -19,
            "applicant_sid": "90155"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -16,
            "applicant_sid": "90156"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -20,
            "applicant_sid": "90157"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -19,
            "applicant_sid": "90158"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -20,
            "applicant_sid": "90159"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -23,
            "applicant_sid": "90160"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -19,
            "applicant_sid": "90161"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -19,
            "applicant_sid": "90162"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -21,
            "applicant_sid": "90163"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -20,
            "applicant_sid": "90164"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -21,
            "applicant_sid": "90165"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -22,
            "applicant_sid": "90166"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -19,
            "applicant_sid": "90167"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -21,
            "applicant_sid": "90168"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -23,
            "applicant_sid": "90169"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -19,
            "applicant_sid": "90170"
        },
        {
            "family_contribution": 2461,
            "need_based_score": 20,
            "applicant_sid": "90171"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -20,
            "applicant_sid": "90172"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -21,
            "applicant_sid": "90173"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -21,
            "applicant_sid": "90174"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -21,
            "applicant_sid": "90175"
        },
        {
            "family_contribution": 629661,
            "need_based_score": 6,
            "applicant_sid": "90176"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -22,
            "applicant_sid": "90177"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -19,
            "applicant_sid": "90178"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -20,
            "applicant_sid": "90179"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -19,
            "applicant_sid": "90180"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -23,
            "applicant_sid": "90181"
        },
        {
            "family_contribution": 0,
            "need_based_score": 22,
            "applicant_sid": "90182"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -22,
            "applicant_sid": "90183"
        },
        {
            "family_contribution": 0,
            "need_based_score": 25,
            "applicant_sid": "90184"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -21,
            "applicant_sid": "90185"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -20,
            "applicant_sid": "90186"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -23,
            "applicant_sid": "90187"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -20,
            "applicant_sid": "90188"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -22,
            "applicant_sid": "90189"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -23,
            "applicant_sid": "90190"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -21,
            "applicant_sid": "90191"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -23,
            "applicant_sid": "90192"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -19,
            "applicant_sid": "90193"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -20,
            "applicant_sid": "90194"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -17,
            "applicant_sid": "90195"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -19,
            "applicant_sid": "90196"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -20,
            "applicant_sid": "90197"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -16,
            "applicant_sid": "90198"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -16,
            "applicant_sid": "90199"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -20,
            "applicant_sid": "90200"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -21,
            "applicant_sid": "90201"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -19,
            "applicant_sid": "90202"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -19,
            "applicant_sid": "90203"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -23,
            "applicant_sid": "90204"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -19,
            "applicant_sid": "90205"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -19,
            "applicant_sid": "90206"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -22,
            "applicant_sid": "90207"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -23,
            "applicant_sid": "90208"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -20,
            "applicant_sid": "90209"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -19,
            "applicant_sid": "90210"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -19,
            "applicant_sid": "90211"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -22,
            "applicant_sid": "90212"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -21,
            "applicant_sid": "90213"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -21,
            "applicant_sid": "90214"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -23,
            "applicant_sid": "90215"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -19,
            "applicant_sid": "90216"
        },
        {
            "family_contribution": 11233,
            "need_based_score": 12,
            "applicant_sid": "90217"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -23,
            "applicant_sid": "90218"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -21,
            "applicant_sid": "90219"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -23,
            "applicant_sid": "90220"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -25,
            "applicant_sid": "90221"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -20,
            "applicant_sid": "90222"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -20,
            "applicant_sid": "90223"
        },
        {
            "family_contribution": 10078,
            "need_based_score": 12,
            "applicant_sid": "90224"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -22,
            "applicant_sid": "90225"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -20,
            "applicant_sid": "90226"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -24,
            "applicant_sid": "90227"
        },
        {
            "family_contribution": 0,
            "need_based_score": 21,
            "applicant_sid": "90228"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -19,
            "applicant_sid": "90229"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -21,
            "applicant_sid": "90230"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -21,
            "applicant_sid": "90231"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -20,
            "applicant_sid": "90232"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -21,
            "applicant_sid": "90233"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -21,
            "applicant_sid": "90234"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -20,
            "applicant_sid": "90235"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -21,
            "applicant_sid": "90236"
        },
        {
            "family_contribution": 46742,
            "need_based_score": 7,
            "applicant_sid": "90237"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -23,
            "applicant_sid": "90238"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -19,
            "applicant_sid": "90239"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -21,
            "applicant_sid": "90240"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -21,
            "applicant_sid": "90241"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -16,
            "applicant_sid": "90242"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -22,
            "applicant_sid": "90243"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -20,
            "applicant_sid": "90244"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -21,
            "applicant_sid": "90245"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -19,
            "applicant_sid": "90246"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -21,
            "applicant_sid": "90247"
        },
        {
            "family_contribution": 47855,
            "need_based_score": 7,
            "applicant_sid": "90248"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -20,
            "applicant_sid": "90249"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -23,
            "applicant_sid": "90250"
        },
        {
            "family_contribution": 34595,
            "need_based_score": 10,
            "applicant_sid": "90251"
        },
        {
            "family_contribution": 2009,
            "need_based_score": 21,
            "applicant_sid": "90252"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -21,
            "applicant_sid": "90253"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -16,
            "applicant_sid": "90254"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -20,
            "applicant_sid": "90255"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -23,
            "applicant_sid": "90256"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -23,
            "applicant_sid": "90257"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -20,
            "applicant_sid": "90258"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -19,
            "applicant_sid": "90259"
        },
        {
            "family_contribution": 85215,
            "need_based_score": 7,
            "applicant_sid": "90260"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -21,
            "applicant_sid": "90261"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -22,
            "applicant_sid": "90262"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -20,
            "applicant_sid": "90263"
        },
        {
            "family_contribution": 0,
            "need_based_score": 25,
            "applicant_sid": "90264"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -21,
            "applicant_sid": "90265"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -20,
            "applicant_sid": "90266"
        },
        {
            "family_contribution": 7429,
            "need_based_score": 12,
            "applicant_sid": "90267"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -22,
            "applicant_sid": "90268"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -23,
            "applicant_sid": "90269"
        },
        {
            "family_contribution": 32094,
            "need_based_score": 11,
            "applicant_sid": "90270"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -19,
            "applicant_sid": "90271"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -20,
            "applicant_sid": "90272"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -23,
            "applicant_sid": "90273"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -19,
            "applicant_sid": "90274"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -19,
            "applicant_sid": "90275"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -19,
            "applicant_sid": "90276"
        },
        {
            "family_contribution": 0,
            "need_based_score": 25,
            "applicant_sid": "90277"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -17,
            "applicant_sid": "90278"
        },
        {
            "family_contribution": 170467,
            "need_based_score": 5,
            "applicant_sid": "90279"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -19,
            "applicant_sid": "90280"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -19,
            "applicant_sid": "90281"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -22,
            "applicant_sid": "90282"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -21,
            "applicant_sid": "90283"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -19,
            "applicant_sid": "90284"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -19,
            "applicant_sid": "90285"
        },
        {
            "family_contribution": -60000,
            "need_based_score": -22,
            "applicant_sid": "90286"
        }
    ]
}
df = pd.DataFrame(d["data"])
ax = df.plot(x='need_based_score', y="family_contribution", kind="scatter", figsize=(9,6))
ax.ticklabel_format(style='plain')
ax.yaxis.set_major_formatter(plt.FormatStrFormatter('%.2f'))
plt.show()