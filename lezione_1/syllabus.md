
Visualizzare le proprietà del singolo switch

``` ovs-ofctl show <switch name> ```


``` ovs-ofctl add-flow <switch name> <match>,<action>```


ovs-ofctl add-flow s1 in_port=1,actions=flood
ovs-ofctl add-flow s1 in_port=2,actions=flood



[Tutorial Ryu](https://osrg.github.io/ryu-book/en/html/index.html)

[datapath object](https://ryu.readthedocs.io/en/latest/ryu_app_api.html#ryu-controller-controller-datapath)