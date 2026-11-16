import re
from collections import Counter

# All questions extracted from 10 papers
papers = {
    "Dec 2021": {
        "1-mark": [
            "The last address of IP address represents ... address (broadcast)",
            "ICMP stands for ...",
            "Network layer firewall works as a ...",
            "SMTP stands for ...",
            "... is the art of manipulating people so they give up confidential information (Social Engineering)",
            "The full form of XSS attack is ...",
            "IPv6 address has a size of ... bits",
            "The practice of creating sub-networks is called ... (subnetting)",
            "... allows the database management system to uniquely identify an entity (Primary Key)",
            "Rows in a RDBMS table denote ... (tuples/records)",
        ],
        "2-mark": [
            "Phishing Attack",
            "Social-networking sites",
            "Impersonation",
            "Cracking",
            "E-mail spoofing",
        ],
        "5-mark": [
            "Describe the types of reverse engineering",
            "Discuss SQL injection attack with the help of a suitable example",
            "What are the privacy and security features being provided by web browsers?",
        ],
        "10-mark": [
            "Explain the extended and base services of server programs",
            "What is database concurrency? What are the methods of database concurrency control? Also, discuss the goals of concurrency control mechanism",
            "List the various categories of cyber attacks. Explain any two of them. Also discuss the ways to counter such attacks",
        ]
    },
    "Jun 2021": {
        "1-mark": [
            "A ______ is an application or device that can read, monitor and capture network packets (Sniffer)",
            "______ is the art of manipulating people so they give up confidential information (Social Engineering)",
            "A ______ is a logically visible subdivision of an IP network (Subnet)",
            "______ allows the Database Management System to uniquely identify (Primary Key)",
            "Sniffing is a technique that could be used to capture network user ______ (passwords)",
            "______ come with various sophisticated tools and techniques to invade a computer and steal personal details of users from their E-mail accounts (Trojans/Keyloggers)",
            "To combine two or more conditions, there is ______ logical operators, where both the conditions are true (AND)",
            "A relational database system needs to maintain data about the relations, such as the schema of the relations. This is called ______ (Data Dictionary)",
            "Firewalls are of two types: Network layer and ______ layer (Application)",
            "Columns in RDBMS tables denote ______ (attributes/fields)",
        ],
        "2-mark": [
            "Explain briefly E-mail spoofing",
            "Explain the difference between Clustering and Mirroring",
            "Explain waste management threats",
            "Give the significance of Distributed Processing",
            "What is data fragmentation?",
        ],
        "5-mark": [
            "Describe social engineering attack cycle",
            "What is the role of Operating System in network security?",
            "Explain Entity-Relationship (ER) model with example",
        ],
        "10-mark": [
            "Explain in detail about Extended and Base services of server programs",
            "Explain in detail the Internet Security Issues",
            "Explain the ACID properties of a database transaction. Which of these is attacked while attempting to breach database security? Justify your answer",
        ]
    },
    "Dec 2022": {
        "5-mark (Section A - 4x5=20)": [
            "Cross-site Scripting (XSS)",
            "White-label Social Networks",
            "Email Bombing",
            "Data Fragmentation",
            "ACID Properties",
        ],
        "5-mark (Section B)": [
            "Explain social engineering attack cycle",
            "Describe Entity-Relationship (ER) model, with example",
            "Discuss OS Password recovery mechanism",
        ],
        "10-mark": [
            "Describe in detail the Internet Security Issues",
            "Explain internal working of a web server",
            "What do you mean by Intruder? Explain the various intrusion techniques in detail",
        ]
    },
    "Jun 2023": {
        "5-mark (Section A - 4x5=20)": [
            "Client/Server architecture",
            "Social Engineering",
            "Cluster table",
            "Social Networking sites",
            "Trojan Horse",
        ],
        "5-mark (Section B)": [
            "Describe the architecture of Oracle Database Management System",
            "Describe SQL injection attack with the help of a suitable example",
            "What is phishing attack? How do you identify a phishing e-mail?",
        ],
        "10-mark": [
            "Explain the security issues involved in centralised as well as distributed database systems. Which one is more insecure and why?",
            "Describe Cross Site Scripting (XSS) and Cross Site Request Forgery (XSRF) attacks and steps to thwart/avoid such attacks",
            "Explain the shadow paging recovery technique",
        ]
    },
    "Dec 2023": {
        "5-mark (Section A - 4x5=20)": [
            "Remote Data Management",
            "Reverse and Social Engineering",
            "Data Dictionary",
            "Waste Management threats",
            "Impersonation",
        ],
        "5-mark (Section B)": [
            "What are the major security issues of social networking sites?",
            "Discuss the advantages of database approach",
            "What is meant by real client server? Explain the types of real client server",
        ],
        "10-mark": [
            "Explain shadow paging recovery technique in detail",
            "Explain Cross Site Scripting (XSS) and Cross Site Request Forgery (XSRF) attacks and steps to avoid such attacks",
            "Explain in detail about extended and base services of server programs",
        ]
    },
    "Jun 2024": {
        "5-mark (Section A - 4x5=20)": [
            "Trojan Horses",
            "Hybrid Crack",
            "Role of scripting language in the cyber world",
            "Entity-Relationship (ER) model",
            "Social bookmarking",
        ],
        "5-mark (Section B)": [
            "Describe the process of using e-mail location tracking tool",
            "Explain SQL injection attack with the help of a suitable example",
            "Discuss social engineering attack cycle",
        ],
        "10-mark": [
            "What is Concurrency Control in a DBMS? What are the methods of concurrency control in a DBMS? Also discuss the goals of concurrency control mechanism",
            "List at least five types of cyber attacks. Explain two of them in detail including the preventive measures that should be adopted to thwart such attacks",
            "Explain the three tier client server architecture with the help of a diagram. Discuss the advantages of three-tier client server architecture over two-tier client server architecture",
        ]
    },
    "Dec 2024": {
        "5-mark (Q1 - 4x5=20)": [
            "Principle of least privilege in access control",
            "Zero-Day Vulnerabilities",
            "Role of Multi-Factor Authentication (MFA)",
            "Social Engineering attacks",
        ],
        "10-mark": [
            "What is domain cache poisoning attack? How can it be prevented?",
            "Explain the architecture and working of a Public Key Infrastructure (PKI)",
            "Describe the steps involved in performing a Vulnerability Assessment and Penetration Testing (VAPT) on a network",
            "Describe the lifecycle of a ransomware attack, from initial infection to encryption and ransom demands",
        ]
    },
    "Jun 2025": {
        "5-mark (Q1 - 4x5=20)": [
            "OWASP top ten vulnerabilities for web application security",
            "Advanced Persistent Threats (APTs)",
            "Botnets",
            "Cloud security and its unique challenges",
        ],
        "10-mark": [
            "How are passwords stored at a server (e.g. at an e-Commerce establishment)? How can hackers get user-passwords by stealing information from the servers?",
            "Explain the key principles and components of the Kerberos authentication protocol. Provide a step-by-step description of how a user can authenticate to a service using Kerberos",
            "Explain the process of a man-in-the-middle (MITM) attack and various techniques used to execute it",
            "Describe the steps involved in securing a cloud computing environment, focusing on Identity and Access Management (IAM), encryption and network security",
        ]
    },
    "Dec 2025": {
        "5-mark (Q1 - 4x5=20)": [
            "Types of Malware (e.g. viruses, worms, trojans)",
            "Importance of VPNs in network security",
            "Concept of Zero-Day Vulnerabilities with examples",
            "Concept of Zero Trust in Information Security",
        ],
        "10-mark": [
            "Explain the principle of least privilege in access control systems. How does it enhance cyber security?",
            "Discuss the steps involved in conducting a Vulnerability Assessment and Penetration Testing (VAPT). Provide examples where VAPT is critical for organisations",
            "Describe the lifecycle of a ransomware attack from initial infection to encryption and ransom demands. What measures can organisations take to prevent such attacks?",
            "What are social engineering attacks? Explain its different types with examples and discuss how individuals and organizations can mitigate such attacks effectively",
        ]
    },
    "Jun 2026": {
        "5-mark (Q1 - 4x5=20)": [
            "Difference between IDS and IPS with examples",
            "Role of Multi-factor Authentication (MFA) in securing systems",
            "Phishing vs. Spear Phishing attacks with example",
            "Steps to prevent domain Cache Poisoning attacks",
        ],
        "10-mark": [
            "Explain Information security in the context of Cloud Infrastructure. How does it ensure secure communication over the Internet?",
            "Discuss how firewalls and intrusion detection systems (IDS) help secure networks from cyber threats. Provide examples of their application in real-world scenarios",
            "What are Zero-Day vulnerabilities? Explain their significance in cyber-security with examples of recent incidents involving zero-day exploits",
            "Describe the importance of conducting regular cyber security audit for organizations to identify vulnerabilities and mitigate risks effectively. Name a commonly referred International standard and provide the steps involved in such audits",
        ]
    }
}

# Count frequency of topics
topic_counter = Counter()
topic_papers = {}
topic_marks = {}

for paper, sections in papers.items():
    for mark_type, questions in sections.items():
        for q in questions:
            q_lower = q.lower()
            topic = ""

            # Categorize questions by key topics
            if any(kw in q_lower for kw in ['social engineering', 'phishing', 'spear phishing', 'impersonation']):
                topic = "Social Engineering"
            elif any(kw in q_lower for kw in ['sql injection', 'sqli']):
                topic = "SQL Injection"
            elif any(kw in q_lower for kw in ['xss', 'cross site scripting', 'xsrf', 'cross site request forgery']):
                topic = "XSS/XSRF"
            elif any(kw in q_lower for kw in ['reverse engineering']):
                topic = "Reverse Engineering"
            elif any(kw in q_lower for kw in ['cracking', 'password recovery', 'password theft', 'hybrid crack']):
                topic = "Cracking/Password Security"
            elif any(kw in q_lower for kw in ['e-mail', 'email', 'spoofing', 'bombing', 'location tracking']):
                topic = "E-mail Security"
            elif any(kw in q_lower for kw in ['trojan', 'malware', 'virus', 'worm', 'botnet', 'apt']):
                topic = "Malware/APT/Botnets"
            elif any(kw in q_lower for kw in ['database', 'dbms', 'concurrency', 'acid', 'er model', 'entity relationship', 'data dictionary', 'fragmentation', 'distributed database', 'shadow paging', 'recovery']):
                topic = "Database Security"
            elif any(kw in q_lower for kw in ['web server', 'client server', 'three tier', 'two tier', 'server program', 'extended service', 'base service']):
                topic = "Web/Client-Server Architecture"
            elif any(kw in q_lower for kw in ['firewall', 'ids', 'ips', 'intrusion', 'intruder']):
                topic = "Network Security (Firewall/IDS/IPS)"
            elif any(kw in q_lower for kw in ['vapt', 'vulnerability assessment', 'penetration testing']):
                topic = "VAPT"
            elif any(kw in q_lower for kw in ['ransomware']):
                topic = "Ransomware"
            elif any(kw in q_lower for kw in ['zero day', 'zero-day']):
                topic = "Zero-Day Vulnerabilities"
            elif any(kw in q_lower for kw in ['pki', 'public key infrastructure', 'kerberos', 'authentication', 'mfa', 'multi-factor', 'least privilege', 'access control']):
                topic = "Authentication/Access Control"
            elif any(kw in q_lower for kw in ['mitm', 'man-in-the-middle', 'man in the middle']):
                topic = "MITM Attack"
            elif any(kw in q_lower for kw in ['cloud', 'cloud security', 'iam']):
                topic = "Cloud Security"
            elif any(kw in q_lower for kw in ['social network', 'social bookmarking', 'white-label']):
                topic = "Social Networking Security"
            elif any(kw in q_lower for kw in ['internet security', 'security issue', 'cyber attack', 'category of cyber attack']):
                topic = "Cyber Attacks/Internet Security Issues"
            elif any(kw in q_lower for kw in ['owasp', 'web application security']):
                topic = "Web Application Security (OWASP)"
            elif any(kw in q_lower for kw in ['cache poisoning', 'domain cache', 'dns']):
                topic = "DNS/Cache Poisoning"
            elif any(kw in q_lower for kw in ['sniffing', 'sniffer', 'network packet']):
                topic = "Network Sniffing"
            elif any(kw in q_lower for kw in ['waste management', 'data fragmentation', 'clustering', 'mirroring', 'distributed processing']):
                topic = "Database Concepts"
            elif any(kw in q_lower for kw in ['ip address', 'icmp', 'smtp', 'ipv6', 'subnet', 'broadcast']):
                topic = "Network Basics"
            elif any(kw in q_lower for kw in ['scripting language', 'client side', 'server side', 'web architecture']):
                topic = "Web Scripting/Architecture"
            elif any(kw in q_lower for kw in ['cyber security audit', 'audit', 'international standard']):
                topic = "Cyber Security Audit"
            elif any(kw in q_lower for kw in ['vpn']):
                topic = "VPN"
            elif any(kw in q_lower for kw in ['zero trust']):
                topic = "Zero Trust"
            elif any(kw in q_lower for kw in ['operating system', 'os password']):
                topic = "OS Security"
            else:
                topic = "Other: " + q[:50]

            topic_counter[topic] += 1
            if topic not in topic_papers:
                topic_papers[topic] = []
            topic_papers[topic].append(paper)
            if topic not in topic_marks:
                topic_marks[topic] = []
            topic_marks[topic].append(mark_type)

# Print analysis
print("=" * 80)
print("TOPIC FREQUENCY ANALYSIS (across 10 papers)")
print("=" * 80)
for topic, count in topic_counter.most_common():
    papers_list = list(set(topic_papers[topic]))
    marks_list = list(set(topic_marks[topic]))
    print(f"\n{topic}: {count} occurrences")
    print(f"  Papers: {', '.join(sorted(papers_list))}")
    print(f"  Marks types: {', '.join(sorted(marks_list))}")

# Also categorize by marks
print("\n\n" + "=" * 80)
print("QUESTIONS BY MARKS CATEGORY")
print("=" * 80)

for paper, sections in papers.items():
    for mark_type, questions in sections.items():
        print(f"\n--- {paper} - {mark_type} ({len(questions)} questions) ---")
        for q in questions:
            print(f"  - {q}")