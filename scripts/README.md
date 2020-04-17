# scripts

## Install the sdk
```bash
pip install --upgrade "ibm-watson>=4.3.0"
```


## This script will create a file for each intent present in the bot and write the answers (only one variation)
```bash
https://cloud.ibm.com/apidocs/assistant/assistant-v2
https://cloud.ibm.com/apidocs/assistant/assistant-v1
```


## Note: 
### this request have a limitation on watson, due to having "export=True" on get_intent method watson only permits 400 calls every 30 minuts
### "With export=false, this operation is limited to 6000 requests per 5 minutes. With export=true, the limit is 400 requests per 30 minutes. For more information, see Rate limiting."


## Necessary: 
have a folder called examples (it is not created automatically in this version) at the same level of the script for storing the result

```bash
|- main folder
    |- examples
    |- get_watson_answers.py
````