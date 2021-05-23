# account.SetContentSettings

Set sensitive content settings (for viewing or hiding NSFW content)



## Example

::::tabs
:::tab{title="JavaScript"}
```js
const {Api, TelegramClient} = require('telegram');
const {StringSession} = require('telegram/sessions');

const session = new StringSession('');
const client = new TelegramClient(session, apiId, apiHash, {});

(async function run() {
    const result = await client.invoke(new Api.account.SetContentSettings({
    sensitiveEnabled: true
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
    const result: Api.Bool = await client.invoke(new Api.account.SetContentSettings({
    sensitiveEnabled: true
}));
    console.log(result); // prints the result
})();
```
:::
::::



## Parameters

| Name | Type | Description |
| :--: | ---- | ----------- |
| **flags** | [#](https://core.telegram.org/type/%23) | Flags, see [TL conditional fields](https://core.telegram.org/mtproto/TL-combinators#conditional-fields) 
| **sensitiveEnabled** | [flags](https://core.telegram.org/mtproto/TL-combinators#conditional-fields).0?[true](https://core.telegram.org/constructor/true) | Enable NSFW content 


## Result

[Bool](https://core.telegram.org/type/Bool)



## Possible errors

| Code | Type | Description |
| :--: | ---- | ----------- |


## Can bots use this method?

Yes

## Related pages

