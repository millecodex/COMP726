[↰ back](../../..)

# Lecture 8: Privacy
## Contents
1. [What is Privacy?](#what-is-privacy)
2. [Privacy Laws](#privacy-laws)
3. [Blockchain Privacy](#blockchain-privacy)
4. [Mixing](#mixing)
5. [Zero Knowledge](#zero-knowledge)
6. [Other Tools](#other-tools)
7. [What did we miss?](#what-did-we-miss)
8. [Further Reading - the very short list](#further-reading---the-very-short-list)
9. [Exercises](#exercises)
10. [Video Lecture](#video-lecture)


## What is Privacy?
### A Definition
In the digital age, privacy transcends its traditional boundaries to become a critical concern in the realm of computer science and information technology. As data becomes the new currency, the right to privacy stands at the intersection of ethical, legal, and technological debates. Within the context of blockchain technology, privacy takes on additional layers of complexity. While blockchain can enhance privacy through decentralisation and cryptographic techniques, its immutable nature also raises questions about data permanence and the right to be forgotten. Hence, understanding privacy as a basic human right is crucial for responsible technological advancement and policy-making.

[Article 12](https://www.un.org/en/about-us/universal-declaration-of-human-rights) of the Universal Declaration of Human Rights (UDHR), adopted in 1948, states:
> "No one shall be subjected to arbitrary interference with his privacy, family, home or correspondence, nor to attacks upon his honour and reputation. Everyone has the right to the protection of the law against such interference or attacks."

### Privacy vs Security
Privacy and security, while closely related, serve distinct roles in the digital landscape. Privacy is primarily concerned with the autonomy individuals have over their personal information—what data is collected, how it is used, and with whom it is shared. Security, on the other hand, focuses on safeguarding that data against unauthorized access and breaches. In the context of blockchain technology, the pseudonymous nature of transactions offers a level of privacy, but it is the blockchain's cryptographic security mechanisms that ensure this data cannot be easily tampered with. Both are indispensable in the construction of robust digital systems, but they address different facets of the information management and safeguarding process.

## Privacy Laws
Laws and regulations designed to safeguard individual privacy vary significantly across national and international boundaries. In the digital realm, these legal frameworks dictate how personal data should be collected, stored, processed, and shared. They aim to strike a balance between technological innovation and the protection of individual rights, particularly in areas like e-commerce, social networking, and emerging technologies such as blockchain.

### GDPR et al.
The General Data Protection Regulation (GDPR) serves as a seminal piece of legislation that has set new global standards for data protection and privacy. Its impact extends beyond the European Union, affecting companies and technologies worldwide. Within the context of blockchain technology, GDPR presents both challenges and opportunities. While blockchain's immutable nature complicates the "right to be forgotten," the technology's built-in security features align well with GDPR's emphasis on data protection.

### Data Sovereignty
Data sovereignty relates to laws and regulations that dictate where data must be stored and processed. These laws vary by jurisdiction and can introduce significant complexities for global technologies like blockchain. For instance, a blockchain network that spans multiple countries must navigate a labyrinth of local and international laws about data residency, potentially affecting the efficiency and legality of cross-border transactions.

## Blockchain Privacy
Blockchain technology has emerged as a revolutionary paradigm for data storage and transactions, offering significant advantages such as decentralisation, transparency, and immutability. However, these strengths also introduce unique privacy challenges. For instance, the transparency and permanence of blockchain transactions can conflict with traditional notions of privacy, such as the ability to erase or modify personal data. Hence, while blockchain holds the promise of enhanced security and user control, it simultaneously raises complex questions concerning data privacy and individual rights.

### Pseudonymous
Blockchain transactions utilise pseudonyms in the form of alphanumeric addresses to represent participants in a transaction. However, it's crucial to understand that pseudonymous does not mean anonymous. Linking a pseudonym to a real-world identity is not straightforward but is possible through techniques such as chain analysis. Therefore, although blockchain provides a higher degree of privacy compared to traditional transaction methods, it does not guarantee full anonymity.

### Metadata
In addition to the primary transaction data, blockchain transactions often include metadata—additional data fields that provide context for the transaction. This metadata can potentially serve as a vector for user identification, especially when correlated with off-chain data or when subjected to sophisticated data analysis techniques. Hence, even if the primary transaction data is pseudonymous, the metadata can inadvertently compromise user privacy.

### Public vs Private Blockchains
Public blockchains are open to anyone and generally offer more transparency, which can be both an advantage and a drawback when it comes to privacy. Private blockchains, on the other hand, are permissioned networks where entry is controlled. Privacy implications vary significantly between the two; for example, a private blockchain might offer more robust data access controls, but it could also be more susceptible to centralized data collection practices, which pose their own set of privacy risks.

### Chainalysis
Chain analysis involves the scrutiny of blockchain data with the aim of tracing digital asset transactions back to individual users. This is done through a variety of techniques, such as clustering algorithms that group together various addresses controlled by a single entity. While useful for legitimate purposes like fraud detection and regulatory compliance, chain analysis poses a significant risk to user privacy, as it can potentially de-anonymise participants in a blockchain network.

## Mixing
Mixing services act as third-party intermediaries that mix different sets of cryptocurrency funds to make it more challenging to trace their original source. These services are particularly relevant in public blockchain networks where transactions are transparent and can be analysed to identify participants. The main objective of mixing services is to obfuscate transaction trails, thereby enhancing privacy and making it difficult to perform chain analysis.

### Tornado Cash:
Tornado Cash is a privacy-focused protocol built on the Ethereum blockchain, designed to break the on-chain link between the source and destination addresses. It uses a smart contract that accepts deposits of a fixed amount and can later make a withdrawal to a different address. Between the deposit and withdrawal steps, cryptographic commitments and zero-knowledge proofs are employed to ensure the process is secure yet untraceable. Thus, Tornado Cash makes it exceedingly difficult to establish any connection between the sending and receiving addresses, thereby enhancing transaction privacy on the Ethereum network.

### How
The principle behind many mixing services is based on algorithms like CoinJoin, which combines multiple payments from multiple spenders into a single transaction. In a typical CoinJoin transaction, it becomes unclear which input (spender) is associated with which output (receiver), making it difficult to trace the origin of the funds. However, it's important to note that while CoinJoin obfuscates the transaction path, it does not make it entirely untraceable. Advanced versions of CoinJoin, like CoinShuffle or CashFusion, add extra layers of privacy by further breaking down and randomly recombining payment amounts.

## Zero Knowledge
Zero-knowledge proofs (ZKPs) are cryptographic techniques that allow one party, known as the prover, to demonstrate to another party, known as the verifier, that a particular statement is true without revealing any specific information about the statement itself. Originating in the late 1980s, ZKPs have become a cornerstone in the realm of cryptographic protocols, particularly in bolstering privacy and security in various applications, including blockchain technology. The fundamental characteristic of a zero-knowledge proof is its ability to maintain the confidentiality of the information being verified, a feature that is increasingly critical in an era of growing concerns about data privacy.

In a zero-knowledge proof, three essential properties must be met: completeness, soundness, and zero-knowledge. Completeness ensures that if the statement is true, the honest verifier will be convinced of its truth by an honest prover. Soundness means that no cheating prover can convince the honest verifier of the truth of a false statement. Lastly, the zero-knowledge property ensures that the verifier gains no additional information from the interaction, apart from the validity of the statement.

In blockchain contexts, ZKPs are often used to enhance transaction privacy. For example, they can prove that a transaction is valid without revealing the amount, sender, or receiver, thereby achieving a balance between transparency and privacy. Overall, zero-knowledge proofs represent a powerful tool for enhancing privacy in digital interactions.

### Alibaba's Cave
The Alibaba's Cave analogy serves as an intuitive way to understand the concept of zero-knowledge proofs. Imagine a cave that is shaped like a 'T', with an entrance at one end and a fork inside that leads to two separate chambers. One chamber contains Alibaba's treasure, and the other is empty. The cave's door can only be opened with a special word, known to the prover but not to the verifier.

In the zero-knowledge context, the prover wants to convince the verifier that they know the secret word to open the treasure chamber, without actually revealing the word itself. The prover enters the cave and chooses either the left or the right path at the fork. The verifier then enters just up to the fork and shouts which path the prover should come out from. If the prover knows the secret word, they can open the door and come out from the path specified by the verifier, proving they know the secret. Importantly, this happens without revealing what the secret word is.

You may now say, "Sure, you just got lucky." This process may be repeated multiple times to reduce the chance of the prover successfully deceiving the verifier by mere luck. After several rounds, the verifier can become statistically convinced that the prover knows the secret, yet the prover hasn't revealed any information about what the secret actually is.

### Where's Waldo (Wally?)
See demonstration.

### zk-SNARKs and zk-STARKs: 
Advanced section. See the What did we miss? section.

## Other Tools
- Homomorphic Encryption: Homomorphic encryption is a sophisticated cryptographic method that allows computations to be performed directly on encrypted data, without the need for decryption. This is particularly advantageous in cloud computing and data analysis scenarios where sensitive information needs to be processed but should not be exposed. For example, a medical research institute could use homomorphic encryption to securely analyse encrypted health data, generating results that can then be decrypted and interpreted, all while maintaining patient confidentiality.
- Multi-Party Computation: MPC is a cryptographic technique that enables multiple parties to jointly compute a function over their inputs while keeping these inputs private from each other. This is extremely useful in scenarios such as secure voting systems, privacy-preserving data analytics, and collaborative scientific research. In essence, each party learns only the specific output and does not gain information about the other parties' individual inputs, thereby preserving privacy and data integrity throughout the computation process.
- Secure Hardware Enclaves: provide isolated execution environments within a computer's hardware where code and data are securely loaded and executed. This isolation ensures that even if the broader system is compromised, the data and operations within the enclave remain inaccessible to outside processes. Such enclaves are often utilised in applications that require stringent security measures, such as digital rights management, secure data storage, and certain blockchain operations.
- Ring Signatures: Used in cryptocurrencies like Monero, ring signatures allow a user to sign a message on behalf of a group. The signature proves the message was created by someone in the group, but it is computationally infeasible to determine which group member's key was used for the signature.
- Confidential Transactions: This method allows for amounts, origins, and destinations of transactions to be obfuscated from the public, yet can be verified to be valid under the network's consensus rules.
- Bulletproofs: These are short non-interactive zero-knowledge proofs that require no trusted setup, making them ideal for blockchain applications where privacy is a concern.
- Schnorr Signatures: These offer a strong level of correctness, do not suffer from malleability, and are also linear, which allows for complex multi-signature schemes not possible with ECDSA.

# What did we miss?
* Decentralised Identity Systems
* zk-SNARKs and zk-STARKs
* Network-level Privacy Dandelion++

# Further Reading - the very short list
* Zcash: History, Privacy, and the Future of Web 3 (w/Zooko Wilcox-O'Hearn & Thomas Walton-Pocock) https://www.youtube.com/watch?v=ibA_4kwd_YI 
* [zk-SNARKs: Under the Hood](https://medium.com/@VitalikButerin/zk-snarks-under-the-hood-b33151a013f6) by Vitalik Buterin: A deep dive into zk-SNARKs and their application in blockchain.
* Blockchain Privacy and Regulatory Compliance: Towards a Practical Equilibrium by Vitalik Buterin et.al (2023). An exploration of privacy issues and solutions in blockchain. ([SSRN](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4563364)) ([pdf](https://github.com/millecodex/COMP842/blob/master/papers/Buterin-Privacy-SSRN-id4563364.pdf))
* [The Dining Cryptographers Problem: Unconditional Sender and Recipient Untraceability](https://link.springer.com/content/pdf/10.1007/BF00206326.pdf) by David Chaum: Introduces the concept of anonymous communication.
* Radiolab Podcast 'The Ceremony' about the ZCash trusted setup https://radiolab.org/podcast/ceremony 

# Exercises
1. a
2. b

# Video Lecture
Here's this lecture recorded live September 18, 2023 on [YouTube](https://www.youtube.com/watch?v=1pK6Iiw0fp0)
