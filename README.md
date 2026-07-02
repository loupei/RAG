The code of the article “Integrating Knowledge Graph with Retrieval-Augmented Generation in Medical Question Answering: Development and Evaluation of MEDQA”.  
Before running the code, you need to install BAAI/bge-m3, Qwen3-8B, GraphDB.  
setup.py - Configuration file.  
embedding.py - KRS data generation embedding.  
llm.py - Invoke Qwen3-8B to generate an answer for the question.  
KBllm.py - Use KRS for retrieval augmented and generate the answer.  
KBKGllm.py - Use KRS, KB for retrieval augmented and generate the answer.  
sparql.py - Have the LLM directly generate SPARQL queries corresponding to the natural language questions.  
cot.py - After adding CoT, have the LLM generate SPARQL queries corresponding to the natural language questions.  
baichuan.py - The Baichuan-M3-Plus model and AntAngelMed model codes used in the evaluation stage.  
