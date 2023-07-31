
# Twitter

This is a Web Twitter Application Developed With Django


## API Reference

#### Get all items

```http
  GET /home
```

```http
  GET /profile_list
```
shows profiles list 

#### Get item

```http
  GET /profile/${id}
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `id`      | `string` | **Required**. Id of item to fetch |


Shows a Particular Profile

```http
  GET /profile/followers|following/${id}
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `id`      | `string` | **Required**. Id of item to fetch |


Shows a Particular Profile's Followers or Following People just Like Actual Instagram 

```http
  GET /login|logout|register
```
Basic Authentications login logout or Registration

#### Get item

```http
  GET /tweet/${id}
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `id`      | `string` | **Required**. Id of item to fetch |

gets a Particular tweet

```http
  GET /tweet_likes/${id}
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `id`      | `string` | **Required**. Id of item to fetch |

like a tweet

```http
  GET /follow|unfollow/${id}
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `id`      | `string` | **Required**. Id of item to fetch |

follow or unfollow a particular profile

#### Get all items

```http
  GET /find_people/
```
search for people around you

## Demo

<img src="https://github.com/idarbandi/Twitter-WV1/blob/650cd3db7b94589d898eb6fa62883890bc96f533/media/screenshots/Screenshot%20from%202023-07-23%2017-18-45.png">
<img src="https://github.com/idarbandi/Twitter-WV1/blob/650cd3db7b94589d898eb6fa62883890bc96f533/media/screenshots/Screenshot%20from%202023-07-23%2017-19-36.png">



