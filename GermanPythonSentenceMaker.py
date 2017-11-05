space = " "
fs = "."
print "What's your subject (person): "
sub=raw_input ()
print "What's your (regular if not sien verb) infinitive: "
inf=raw_input ()
inf=inf[0:len(inf)-2]
print "What were you doing (related to your verb): "
act=raw_input ()

print "Do you want to form a present tense sentence (p), a past tense sentence with haben (h) or a past tense sentence with sein (s)? "
ans=raw_input()
if ans == "p":
	if sub == "Ich":
		print "First we have the subject: "+sub+"\nThen we have the conjugated verb (take 'en' off and add 'e' for Ich): "+inf+"e"+"\nThen we have the action: "+act+"\nThe product is: "+sub+space+inf+"e"+space+act+fs
	elif sub == "Du": 
		print "First we have the subject:"+sub+"\nThen we have the conjugated verb (take 'en' off and add 'st' for Du): "+inf+"st"+"\nThen we have the action: "+act+"\nThe product is: "+sub+space+inf+"st"+space+act+fs
	elif sub == "Er":
		print "First we have the subject: "+sub+"\nThen we have the conjugated verb (take 'en' off and add 't' for Er): "+inf+"t"+"\nThen we have the action: "+act+"\nThe product is: "+sub+space+inf+"t"+space+act+fs
	elif sub == "Sie":
		print "First we have the subject: "+sub+"\nThen we have the conjugated verb (take 'en' off and add 't' for Sie): "+inf+"t"+"\nThen we have the action: "+act+"\nThe product is: "+sub+space+inf+"t"+space+act+fs
	elif sub == "Es":
		print "First we have the subject: "+sub+"\nThen we have the conjugated verb (take 'en' off and add 't' for Es): "+inf+"t"+"\nThen we have the action: "+act+"\nThe product is: "+sub+space+inf+"t"+space+act+fs
	elif sub == "Wir":
		print "First we have the subject: "+sub+"\nThen we have the conjugated verb (take 'en' off and add 'en' for Wir): "+inf+"en"+"\nThen we have the action: "+act+"\nThe product is: "+sub+space+inf+"en"+space+act+fs
	elif sub == "Ihr":
		print "First we have the subject: "+sub+"\nThen we have the conjugated verb (take 'en' off and add 't' for Ihr): "+inf+"t"+"\nThen we have the action: "+act+"\nThe product is: "+sub+space+inf+"t"+space+act+fs
elif ans == "h":
	if sub == "Ich": 
		print "First we have the subject: "+sub+"\nThen we have the form of haben for that subject: "+"habe"+"\nThen we have the action: "+act+"\nThen we have the past participle of your verb (you add 'ge' to the start, then take 'en' off the end and add 't' for regular verbs) at the end: "+"ge"+inf+"t"+"\nThe product is: "+sub+space+"habe"+space+act+space+"ge"+inf+"t"+fs
	elif sub == "Du": 
		print "First we have the subject: "+sub+"\nThen we have the form of haben for that subject: "+"hast"+"\nThen we have the action: "+act+"\nThen we have the past participle of your verb (you add 'ge' to the start, then take 'en' off the end and add 't' for regular verbs) at the end: "+"ge"+inf+"t"+"\nThe product is: "+sub+space+"hast"+space+act+space+"ge"+inf+"t"+fs
	elif sub == "Er": 
		print "First we have the subject: "+sub+"\nThen we have the form of haben for that subject: "+"hat"+"\nThen we have the action: "+act+"\nThen we have the past participle of your verb (you add 'ge' to the start, then take 'en' off the end and add 't' for regular verbs) at the end: "+"ge"+inf+"t"+"\nThe product is: "+sub+space+"hat"+space+act+space+"ge"+inf+"t"+fs
	elif sub == "Sie": 
		print "First we have the subject: "+sub+"\nThen we have the form of haben for that subject: "+"hat"+"\nThen we have the action: "+act+"\nThen we have the past participle of your verb (you add 'ge' to the start, then take 'en' off the end and add 't' for regular verbs) at the end: "+"ge"+inf+"t"+"\nThe product is: "+sub+space+"hat"+space+act+space+"ge"+inf+"t"+fs
	elif sub == "Es": 
		print "First we have the subject: "+sub+"\nThen we have the form of haben for that subject: "+"hat"+"\nThen we have the action: "+act+"\nThen we have the past participle of your verb (you add 'ge' to the start, then take 'en' off the end and add 't' for regular verbs) at the end: "+"ge"+inf+"t"+"\nThe product is: "+sub+space+"hat"+space+act+space+"ge"+inf+"t"+fs
	elif sub == "Wir": 
		print "First we have the subject: "+sub+"\nThen we have the form of haben for that subject: "+"haben"+"\nThen we have the action: "+act+"\nThen we have the past participle of your verb (you add 'ge' to the start, then take 'en' off the end and add 't' for regular verbs) at the end: "+"ge"+inf+"t"+"\nThe product is: "+sub+space+"haben"+space+act+space+"ge"+inf+"t"+fs
	elif sub == "Ihr": 
		print "First we have the subject: "+sub+"\nThen we have the form of haben for that subject: "+"habt"+"\nThen we have the action: "+act+"\nThen we have the past participle of your verb (you add 'ge' to the start, then take 'en' off the end and add 't' for regular verbs) at the end: "+"ge"+inf+"t"+"\nThe product is: "+sub+space+"habt"+space+act+space+"ge"+inf+"t"+fs
elif ans == "s":
  if inf == "schwimm":
    inf = "geschwommen"
  if inf == "geh":
    inf = "gegangen"
  if inf == "bleib":
    inf = "geblieben"
  if inf == "flieg":
    inf = "geflogen"
  if inf == "fahr":
  	inf = "gefahren"
  if sub == "Ich": 
		print "First we have the subject: "+sub+"\nThen we have the form of sein for that subject (as this is a verb that requires sein): "+"bin"+"\nThen we have the action: "+act+"\nThen we have the past participle of your verb (As sein verbs are irregular, these follow no pattern) at the end: "+inf+"\nThe product is: "+sub+space+"bin"+space+act+space+inf+fs
  elif sub == "Du": 
		print "First we have the subject: "+sub+"\nThen we have the form of sein for that subject (as this is a verb that requires sein): "+"bist"+"\nThen we have the action: "+act+"\nThen we have the past participle of your verb (As sein verbs are irregular, these follow no pattern) at the end: "+inf+"\nThe product is: "+sub+space+"bist"+space+act+space+inf+fs
  elif sub == "Er": 
		print "First we have the subject: "+sub+"\nThen we have the form of sein for that subject (as this is a verb that requires sein): "+"ist"+"\nThen we have the action: "+act+"\nThen we have the past participle of your verb (As sein verbs are irregular, these follow no pattern) at the end: "+inf+"\nThe product is: "+sub+space+"ist"+space+act+space+inf+fs
  elif sub == "Sie": 
		print "First we have the subject: "+sub+"\nThen we have the form of sein for that subject (as this is a verb that requires sein): "+"ist"+"\nThen we have the action: "+act+"\nThen we have the past participle of your verb (As sein verbs are irregular, these follow no pattern) at the end: "+inf+"\nThe product is: "+sub+space+"ist"+space+act+space+inf+fs
  elif sub == "Es": 
		print "First we have the subject: "+sub+"\nThen we have the form of sein for that subject (as this is a verb that requires sein): "+"ist"+"\nThen we have the action: "+act+"\nThen we have the past participle of your verb (As sein verbs are irregular, these follow no pattern) at the end: "+inf+"\nThe product is: "+sub+space+"ist"+space+act+space+inf+fs
  elif sub == "Wir": 
		print "First we have the subject: "+sub+"\nThen we have the form of sein for that subject (as this is a verb that requires sein): "+"sind"+"\nThen we have the action: "+act+"\nThen we have the past participle of your verb (As sein verbs are irregular, these follow no pattern) at the end: "+inf+"\nThe product is: "+sub+space+"sind"+space+act+space+inf+fs
  elif sub == "Ihr": 
		print "First we have the subject: "+sub+"\nThen we have the form of sein for that subject (as this is a verb that requires sein: "+"seid"+"\nThen we have the action: "+act+"\nThen we have the past participle of your verb (As sein verbs are irregular, these follow no pattern) at the end: "+inf+"\nThe product is: "+sub+space+"seid"+space+act+space+inf+fs