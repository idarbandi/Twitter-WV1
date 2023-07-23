
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

media/screenshots/Screenshot from 2023-07-23 17-18-45.png

media/screenshots/Screenshot from 2023-07-23 17-19-36.png


