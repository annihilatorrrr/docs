# account.SendConfirmPhoneCode

Send confirmation code to cancel account deletion, for more info [click here »](https://core.telegram.org/api/account-deletion)



## Example

::::tabs
:::tab{title="JavaScript"}
```js
const {Api, TelegramClient} = require('telegram');
const {StringSession} = require('telegram/sessions');

const session = new StringSession('');
const client = new TelegramClient(session, apiId, apiHash, {});

(async function run() {
    const result = await client.invoke(new Api.account.SendConfirmPhoneCode({
    hash: 'B5MnlS34H1JKyBE71zZfo1',
    settings: new Api.CodeSettings({
        allowFlashcall: true,
        currentNumber: true,
        allowAppHash: true
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
    const result: Api.auth.SentCode = await client.invoke(new Api.account.SendConfirmPhoneCode({
    hash: 'B5MnlS34H1JKyBE71zZfo1',
    settings: new Api.CodeSettings({
        allowFlashcall: true,
        currentNumber: true,
        allowAppHash: true
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
| **hash** | [string](https://core.telegram.org/type/string) | The hash from the service notification, for more info [click here »](https://core.telegram.org/api/account-deletion) 
| **settings** | [CodeSettings](https://core.telegram.org/type/CodeSettings) | Phone code settings 


## Result

[auth.SentCode](https://core.telegram.org/type/auth.SentCode)



## Possible errors

| Code | Type | Description |
| :--: | ---- | ----------- |
| 400 | HASH\_INVALID | The provided hash is invalid 


## Can bots use this method?

Yes

## Related pages

#### [Account deletion](https://core.telegram.org/api/account-deletion)

How to reset an account if the 2FA password was forgotten.



