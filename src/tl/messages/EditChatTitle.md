# messages.EditChatTitle

Chanages chat name and sends a service message on it.



## Example

::::tabs
:::tab{title="JavaScript"}
```js
const {Api, TelegramClient} = require('telegram');
const {StringSession} = require('telegram/sessions');

const session = new StringSession('');
const client = new TelegramClient(session, apiId, apiHash, {});

(async function run() {
    const result = await client.invoke(new Api.messages.EditChatTitle({
    chatId: 43,
    title: 'My very normal title'
}));
    console.log(result); // prints the result
})();
```
:::

:::tab{title="TypeScript"}
```ts
import {Api, TelegramClient} from 'telegram';
import {StringSession} from 'telegram/sessions';

const session = new StringSession('');
const client = new TelegramClient(session, apiId, apiHash, {});

(async function run() {
    const result: Api.Updates = await client.invoke(new Api.messages.EditChatTitle({
    chatId: 43,
    title: 'My very normal title'
}));
    console.log(result); // prints the result
})();
```
:::
::::



## Parameters

| Name | Type | Description |
| :--: | ---- | ----------- |
| **chatId** | [int](https://core.telegram.org/type/int) | Chat ID 
| **title** | [string](https://core.telegram.org/type/string) | New chat name, different from the old one 


## Result

Returns a [messages.StatedMessage](https://core.telegram.org/type/messages.StatedMessage) object containing a service message sent during an action.



## Possible errors

| Code | Type | Description |
| :--: | ---- | ----------- |
| 400 | CHAT\_ID\_INVALID | The provided chat id is invalid 
| 400 | CHAT\_NOT\_MODIFIED | The pinned message wasn't modified 
| 400 | CHAT\_TITLE\_EMPTY | No chat title provided 
| 400 | PEER\_ID\_INVALID | The provided peer id is invalid 


## Can bots use this method?

Yes

## Related pages

