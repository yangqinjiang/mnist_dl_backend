# mnist_dl_backend
mnist deeplearning backend
```运行环境
python 3.7
flask
numpy

```

```
API:  /v1/guess
input:
{
	"input":{}
}


output:
{
    "code": 1,
    "data": {
        "number": 1,
        "softmax_result": [
            {
                "index": 0,
                "value": 0.43016675264768545
            },
            {
                "index": 1,
                "value": 0.983090819257726
            },
            {
                "index": 2,
                "value": 0.5490988117955813
            },
            {
                "index": 3,
                "value": 0.6736779994092721
            },
            {
                "index": 4,
                "value": 0.5075336770378582
            },
            {
                "index": 5,
                "value": 0.7487281152258365
            },
            {
                "index": 6,
                "value": 0.2867309295281756
            },
            {
                "index": 7,
                "value": 0.3781404196550565
            },
            {
                "index": 8,
                "value": 0.22591494055815753
            },
            {
                "index": 9,
                "value": 0.45859884585798794
            }
        ]
    }
}

```