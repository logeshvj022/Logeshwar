#question:answer

qua={

    "hi":"hello",
    "how are you":"i am fine",
    "what is your name":"My name is jarvis",
    "how old are you?":"i am 20 years old",
    "what is your favorite color?":"violet",
    "where are you from?":"mettupalayam",
    "do you have a girlfriend?":"no",
    "which is your nataive place":"coimbatore",
    "let's meet you":"if time permits",
    "what do you do":"i study",
    "which university":"barathiyar university",
    "what is your aim?":"software engineer",
    "hi are you there?":"yes i am here",
    "how is monsoon today?":"yah it is good",
    "it's rainy today":"yes",
    "how about going to ride?":"its horse ride",
    "are you human?":"no",
    "are you robot?":"yes",
    "whick languages can you speak?":"english",
    "I have a question?":"yah tell me",
    "do you know a joke?":"yes",
    "do you love me?":"no no",
    "will you marry me?":"i am already married",
    "are you single?":"i am always morratu single",
    "do you like people?":"yes",
    "do you have a hobby?":"yes",
    "tell me about your hobby?":"software developer",
    "are you expensive?":"yes",
    "what is bot?":"A bot is a software program that operates on the Internet and performs repetitive tasks. While some bot traffic is from good bots, bad bots can have a huge negative impact on a website or application",
    "types of bots?":"\n1.spider bots,"
                     "\n2.scraper bots,"
                     "\n3.spam bots,"
                     "\n4.social media bots,"
                     "\n5.download bots,"
                     "\n6.ticketing bots,"
                     "\n7.malicious and non malicious bot activity\n",
    "1":"A web crawler, or spider, is a type of bot that is typically operated by search engines like Google and Bing. Their purpose is to index the content of websites all across the Internet so that those websites can appear in search engine results",
    "2":"Scraper tools and bots — Web scraping is the process of using bots to extract content and data from a website. Unlike screen scraping, which only",
    "3":"A spambot is a computer program designed to assist in the sending of spam. Spambots usually create accounts and send spam messages with them",
    "4":"Broadly speaking, social media bots are automated programs used to engage in social media. These bots behave in an either partially or fully autonomous fashion, and are often designed to mimic human users. While benevolent social media bots exist, many social media bots are used in dishonest and nefarious ways.",
    "5":"A bot definition defines the steps that are needed to implement a bot in IBM® Robotic Process Automation (IBM RPA) with Automation Anywhere. It is generated from a robot task in a process and can be downloaded and then imported into IBM RPA.",
    "6":"Ticket bots are a type of bot that carries out tasks related to ticketing, such as scraping pricing details, checking inventory for newly released seats, or purchasing tickets",
    "7":"A malicious bot is malware designed to steal information, or infect a host, often used by cyber criminals. The threat of these automated programs can come in many forms; DDOS, spam, content duplication,",
    "hi chatbot":" \n1 What Are Chatbots"
    "\n1.1 Some examples of chatbots"
    "\n1.2 What can chatbots do"
    "\n1.3 How can chatbots improve business"
    "\n1.4 Some use cases of chatbots",
    "1.1":"*Liveperson,\n*LiveChat,\n*Amazon Lex,\n*Dialogflow,\n*IBM Watson,\n*bold360",
    "1.2":""
}

print("\033[1;35m This text is bright magenta\n")
print("\033[0;37;40m chatbot \n")
print("\033[1;35;40m \033[2;36:40m TextColour Bright Magenta          TextColour Bright CyanBackground                yellow ColouredBackground\033[0;36;40m\n")


while True:
    qs = input()

    if(qs == "quit"):
        break

    else:
        print(qua[qs])

