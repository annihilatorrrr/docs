# channels.SetStickers

Associate a stickerset to the supergroup



## Example

::::tabs
:::tab{title="JavaScript"}
```js
const {Api, TelegramClient} = require('telegram');
const {StringSession} = require('telegram/sessions');

const session = new StringSession('');
const client = new TelegramClient(session, apiId, apiHash, {});

(async function run() {
    const result = await client.invoke(new Api.channels.SetStickers({
    channel: 'username',
    stickerset: new Api.InputStickerSetID({
        id: BigInt('-4156887774564'),
        accessHash: BigInt('-4156887774564')
    })
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
    const result: Api.Bool = await client.invoke(new Api.channels.SetStickers({
    channel: 'username',
    stickerset: new Api.InputStickerSetID({
        id: BigInt('-4156887774564'),
        accessHash: BigInt('-4156887774564')
    })
}));
    console.log(result); // prints the result
})();
```
:::
::::



## Parameters

| Name | Type | Description |
| :--: | ---- | ----------- |
| **channel** | [InputChannel](https://core.telegram.org/type/InputChannel) | Supergroup 
| **stickerset** | [InputStickerSet](https://core.telegram.org/type/InputStickerSet) | The stickerset to associate 


## Result

[Bool](https://core.telegram.org/type/Bool)



## Possible errors

| Code | Type | Description |
| :--: | ---- | ----------- |
| 400 | CHANNEL\_INVALID | The provided channel is invalid 
| 400 | PARTICIPANTS\_TOO\_FEW | Not enough participants 


## Can bots use this method?

Yes

## Related pages

