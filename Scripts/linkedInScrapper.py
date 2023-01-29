import requests
import json
import re

domains_list = ["Cyber+Security","Android+App+Development","Graphic+Designer","Web+Developer","Aritificial+Intelligence","Animation","Digital+Marketing"]

SEARCH_URL = "https://www.linkedin.com/voyager/api/search/dash/clusters?decorationId=com.linkedin.voyager.dash.deco.search.SearchClusterCollection-174&origin=GLOBAL_SEARCH_HEADER&q=all&query=(keywords:{},flagshipSearchIntent:SEARCH_SRP,queryParameters:(resultType:List(PEOPLE)),includeFiltersInResponse:false)&start={}"

PROFILE_URL = "https://www.linkedin.com/voyager/api/graphql?includeWebMetadata=true&variables=(profileUrn:{})&&queryId=voyagerIdentityDashProfileCards.baf818a9b234685b3e289531cfccf0f9"

headers = {
"Cookie": """bcookie="v=2&57c20411-00d6-46a1-83f5-88f1cfbef047"; li_sugr=7ccd0e97-4e7b-4d0d-8365-5feb6f509776; bscookie="v=1&202209121326583c519841-22ff-4665-8dbe-d57e46c08208AQHT2MQk9ywjxzbA_FFp9kEZ5uCLHF6p"; li_rm=AQFw_8p9qA1pGQAAAYNTnOR0gopRvIjhljX0s2diI9NKDjk1jOG8_xZibegIn5edrbkqo5pNJkqY1dGYL5Gi-JjHxo2mngiXijcehjgkm-VnLLInfBrP7xaT; G_ENABLED_IDPS=google; li_theme=light; li_theme_set=app; timezone=Asia/Karachi; AnalyticsSyncHistory=AQIy-7hMFlri8gAAAYUe8i3f-tUklB9KxxOjGU3R33GEqsXFgF-5kUYyN8N2hkOATUhzTFk5xahngqq8S8bz3g; lms_ads=AQGkNOWL1Xp0XgAAAYUe8kHzKSWcmiGdxkOMTxUvOqzD4VWQGvd2y7FNIHkKZVshWmpwFYTQJqzlJBAPf7-AlyLwPzl1XQJs; lms_analytics=AQGkNOWL1Xp0XgAAAYUe8kHzKSWcmiGdxkOMTxUvOqzD4VWQGvd2y7FNIHkKZVshWmpwFYTQJqzlJBAPf7-AlyLwPzl1XQJs; visit=v=1&M; g_state={"i_l":1,"i_p":1671439779432}; fid=AQHQnHfUxqkK6wAAAYUpJjPm6oGnRFY0sJ7AxS4NwbgO0M3DzTo0DHk6DsRpG6WG8Rhb7f1i9wH6_Q; li_at=AQEDAT-ajOsEmFGuAAABhSkm9JoAAAGFTTN4mlYAXTwzBa4dOSfx_H6751TRBliW3i6T_CjyHTJLc0XoaT30zY1tUM_Pzbw2cRUKr7EOo5J_IWkZNXx669fj9cMZiz8806DFA7cAM17ivENIpCirCS_e; liap=true; JSESSIONID="ajax:8677270665568837287"; fcookie=AQEcNjC5Msc3ZQAAAYUpJw5zwOVgoO00d8bsiRNm4sCaUHLlRF2kUZFqtvvrKTSGh9nW5cUIzYSUEB9hz4cqH47MiLRo73LIkP-Es5Q-mvKhg7-QRMeotMaC5AWO1hOO69l57dqTDiM8VyG1k4y6d6B62xshU-BLTjTUAgJHqxancq0mp1h8SB9f7UV1GvSGAJxZ2kPx6opLW4_V-xfQOKs7fesqK66D6H6pFohd_z-Kjp646HuqNJaF6gSp9ZFgyfMVXQdqW14jbUBpF0rJs88pyd0s2ZYDE7QQPa7OZj3jX5Vup95eRMihgGDYI6tmm5S/8j32oy2MdGJkqgapmxy1v5Lw==; lang=v=2&lang=en-us; UserMatchHistory=AQJmziCrBVoXhgAAAYUpgHcvtf5UsloZyZLFI5fZLeDnY_XiI1pHaXjqr37QQjR4PVMY3iINuEQXQxh0Feb4cEsDSAxMnaDqJHJL2DDa_QDh2gPXI7itjTybGDeCqaw9Plo77YKwwpIsm-p6M9hbU0tYT5d5oqtPleGQT0C4ta_WKHgZciduQAzN7PTu95fwYNsRbx6INfUlEThqzXTPVmZLPDT6f_kH8PR430Ru4ffvm2D6IuFCQwCGBUleRR6Wx5J2yFR57cKMBYDh_j70PSkEyX0TQS4ttZ5gBYY; lidc="b=VB27:s=V:r=V:a=V:p=V:g=4093:u=8:x=1:i=1671438564:t=1671483276:v=2:sig=AQHYsAmd0at-GTYQ2kcU6szqy_hn2Yb1"; AMCVS_14215E3D5995C57C0A495C55%40AdobeOrg=1; AMCV_14215E3D5995C57C0A495C55%40AdobeOrg=-637568504%7CMCIDTS%7C19346%7CMCMID%7C87304354250308140793385128131920702125%7CMCAAMLH-1672043365%7C3%7CMCAAMB-1672043365%7C6G1ynYcLPuiQxYZrsz_pkqfLG9yMXBpb2zX5dvJdYQJzPXImdj0y%7CMCOPTOUT-1671445765s%7Cpartner%2Cpartner%7CvVersion%7C5.1.1%7CMCCIDH%7C1987539808""",
"Sec-Ch-Ua": """"Not?A_Brand";v="8", "Chromium";v="108", "Microsoft Edge";v="108""",
"X-Li-Lang": "en_US",
"Sec-Ch-Ua-Mobile": "?0",
"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 Edg/108.0.1462.46",
"X-Li-Page-Instance": "urn:li:page:d_flagship3_search_srp_people;V4nyE999RtWVz7pxbk2byA==",
"Accept": "application/vnd.linkedin.normalized+json+2.1",
"Csrf-Token": "ajax:8677270665568837287",
"X-Li-Track": """{"clientVersion":"1.11.5633","mpVersion":"1.11.5633","osName":"web","timezoneOffset":5,"timezone":"Asia/Karachi","deviceFormFactor":"DESKTOP","mpName":"voyager-web","displayDensity":1,"displayWidth":1366,"displayHeight":768}""",
"X-Restli-Protocol-Version": "2.0.0",
"Sec-Ch-Ua-Platform": "Windows",
"Sec-Fetch-Site": "same-origin",
"Sec-Fetch-Mode": "cors",
"Sec-Fetch-Dest": "empty",
"Referer": """https://www.linkedin.com/search/results/people/?keywords=cyber+ecurity&origin=GLOBAL_SEARCH_HEADER&sid=(rK""",
"Accept-Encoding": "gzip, deflate",
"Accept-Language": "en-US,en;q=0.9"
}

dataset = []

for domain in domains_list:

    for search_start_no in range(1,200,10):

        username = ""
        
        user_about = ""
        
        response = requests.get(url=SEARCH_URL.format(domain,search_start_no), headers=headers)

        json_data = json.loads(response.text)
        
        users_data = json_data["included"]

        # json data contain user informations ::[start -> index = 10+1] [end -> json_data_length - 10]
        
        for user_no in range(11,len(users_data)-9):

            user = users_data[user_no]

            for x in user:

                #In order to see keys of user's data
                
                print(x)

            try:

                username = user["title"]["text"]

                print(username)
                
                print(user["navigationUrn"])
                
                # print(user["entityUrn"])
                
                profile_urn = re.findall("[(].*[,]",user["entityUrn"])[0][1:-12].replace(":","%3A")

                about_response = requests.get(url=PROFILE_URL.format(profile_urn),headers=headers)

                about_json_data = json.loads(about_response.text)

            except:

                pass

            for x in about_json_data["included"]:

                try:
                    
                    user_about = x["topComponents"][1]["components"]["textComponent"]["text"]["text"]
                    
                    print(user_about)

                except:

                    pass
            
            if user_about != "" and user_about != None:

                user_entry = {"username":username, "user_about":user_about}

                dataset.append(user_entry)

                with open("linkedInData.json", "w") as output_file:

                    output_file.write(json.dumps(dataset))

                # Clearing data in variables, so that data don't get duplicate

                username = ""
                
                user_about = ""







    



