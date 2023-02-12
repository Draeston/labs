# Manual approach

```
pod/python-app-869dc76fc7-tkj7t   1/1     Running   0          45s

NAME                 TYPE           CLUSTER-IP       EXTERNAL-IP   PORT(S)          AGE
service/kubernetes   ClusterIP      10.96.0.1        <none>        443/TCP          66s
service/python-app   LoadBalancer   10.106.114.165   <pending>     8080:30398/TCP   16s
```

# Config approach

```
NAME                                         READY   STATUS    RESTARTS   AGE
pod/python-app-deployment-7dd784648c-9mg78   1/1     Running   0          75s
pod/python-app-deployment-7dd784648c-jldvb   1/1     Running   0          75s
pod/python-app-deployment-7dd784648c-lnbcz   1/1     Running   0          75s

NAME                 TYPE           CLUSTER-IP       EXTERNAL-IP   PORT(S)          AGE
service/kubernetes   ClusterIP      10.96.0.1        <none>        443/TCP          13m
service/python-app   LoadBalancer   10.108.134.239   <pending>     8080:31471/TCP   75s
```

```
|-----------|------------|-------------|--------------|
| NAMESPACE |    NAME    | TARGET PORT |     URL      |
|-----------|------------|-------------|--------------|
| default   | kubernetes |             | No node port |
|-----------|------------|-------------|--------------|
😿  service default/kubernetes has no node port
|-----------|------------|-------------|---------------------------|
| NAMESPACE |    NAME    | TARGET PORT |            URL            |
|-----------|------------|-------------|---------------------------|
| default   | python-app |        8080 | http://192.168.49.2:31471 |
|-----------|------------|-------------|---------------------------|
🏃  Starting tunnel for service kubernetes.
🏃  Starting tunnel for service python-app.
|-----------|------------|-------------|------------------------|
| NAMESPACE |    NAME    | TARGET PORT |          URL           |
|-----------|------------|-------------|------------------------|
| default   | kubernetes |             | http://127.0.0.1:54335 |
| default   | python-app |             | http://127.0.0.1:54337 |
|-----------|------------|-------------|------------------------|
🎉  Opening service default/kubernetes in default browser...
🎉  Opening service default/python-app in default browser...
❗  Because you are using a Docker driver on windows, the terminal needs to be open to run it.
```

![Screenshot](screenshot.png)

