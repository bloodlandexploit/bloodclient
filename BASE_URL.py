import ConnectEntities
main_server = "https://api.blood.land/mining/servers/9"


Dump_CE = ConnectEntities.ConnectEntry(main_server)
secret_key_1 = Dump_CE[0]
apiurl = Dump_CE[1]
miningurl = Dump_CE[2]
code = Dump_CE[3]
tokenurl = apiurl+"bijfuwt7fhqo"
bannerurl = apiurl+"gk9qbiq1cmc9?lang=kr"
infourl = apiurl+"amicurnbc31f"
listmsgurl = apiurl+"ikr8917nyx3q"
reporturl = apiurl+"ofu8a3qum813"