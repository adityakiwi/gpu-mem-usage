# Basic MNIST Example

```bash
pip install -r requirements.txt
python main.py
# CUDA_VISIBLE_DEVICES=2 python main.py  # to specify GPU id to ex. 2
```

# On your laptop
  scp -r <remote>:<directory>/log .

  launch chrome or MS edge browser, enter address: 
```
chrome://tracing
```

  Then "load", find one of the JSON files under the copied "log" directory.


# reference: 

https://www.chromium.org/developers/how-tos/trace-event-profiling-tool/trace-event-reading/
	
https://pytorch.org/tutorials/intermediate/tensorboard_profiler_tutorial.html
