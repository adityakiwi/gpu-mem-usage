# gpu-mem-usage
A few quick ways to find out memory usage on GPU

# multiple ways to figure out the memory usages of GPU

## nvidia-smi

## nvidia-smi dmon -d 1 -s pucmt -o T
        (nvidia-smi dmon --help)

## torch.cuda functions
        torch.cuda.memory_allocated
        torch.cuda.memory_reserved

    pip3 install -r requirements.txt
    python3 gpumem.py

## GPUtil package

    pip3 install -r requirements.txt
    python3 memreport.py
