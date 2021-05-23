# channels.GetParticipant

Get info about a [channel/supergroup](https://core.telegram.org/api/channel) participant



## Example

::::tabs
:::tab{title="JavaScript"}
```js
const {Api, TelegramClient} = require('telegram');
const {StringSession} = require('telegram/sessions');

const session = new StringSession('');
const client = new TelegramClient(session, apiId, apiHash, {});

(async function run() {
    const result = await client.invoke(new Api.channels.GetParticipant({
    channel: 'username',
    userId: 'username'
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
    const result: Api.channels.ChannelParticipant = await client.invoke(new Api.channels.GetParticipant({
    channel: 'username',
    userId: 'username'
}));
    console.log(result); // prints the result
})();
```
:::
::::



## Parameters

| Name | Type | Description |
| :--: | ---- | ----------- |
| **channel** | [InputChannel](https://core.telegram.org/type/InputChannel) | Channel/supergroup 
| **userId** | [InputUser](https://core.telegram.org/type/InputUser) | ID of participant to get info about 


## Result

[channels.ChannelParticipant](https://core.telegram.org/type/channels.ChannelParticipant)



## Possible errors

| Code | Type | Description |
| :--: | ---- | ----------- |
| 400 | CHANNEL\_INVALID | The provided channel is invalid 
| 400 | CHANNEL\_PRIVATE | You haven't joined this channel/supergroup 
| 400 | CHAT\_ADMIN\_REQUIRED | You must be an admin in this chat to do this 
| 400 | MSG\_ID\_INVALID | Invalid message ID provided 
| 400 | USER\_ID\_INVALID | The provided user ID is invalid 
| 400 | USER\_NOT\_PARTICIPANT | You're not a member of this supergroup/channel 


## Can bots use this method?

Yes

## Related pages

#### [Channels](https://core.telegram.org/api/channel)

How to handle channels, supergroups, groups, and what's the difference between them.



