from llama_index import VectorStoreIndex
from llama_index.schema import TextNode
from text2speech import txt2speech
from inference import main

import openai
import pickle
def master(query,l):
    openai.api_key="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"

    f=open("data.txt","rb")
    d=pickle.load(f)

    nodes=[TextNode(text=transcript['text'], id_=transcript['id']) for transcript in d]

    index = VectorStoreIndex(nodes)
    query_engine = index.as_query_engine()

    #query = 'what are etfs? Answer this in kannada'
    print("done1")
    response = query_engine.query(query)
    c = response.response
    with open("temp.txt","wb+") as f:
        pickle.dump(c,f)
    txt2speech(c,l)
    print("done2")
    main()