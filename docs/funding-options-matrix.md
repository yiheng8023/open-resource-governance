# Funding Options Matrix

This document tracks possible funding channels for a small, public-safe open
source project. It is an evaluation aid, not a claim that every channel is
active.

The default rule is conservative:

```text
evaluate channel
-> verify owner control
-> verify logged-out public URL
-> verify payout path
-> check privacy and compliance implications
-> update FUNDING.yml only after activation
```

## Current recommendation

Do not rush to enable every payment surface.

For maintainers without a supported overseas bank account or credit card, the
most practical order is:

1. keep GitHub's Sponsor/Funding button pointed at
   [`support-and-sponsorship.md`](support-and-sponsorship.md);
2. evaluate GitHub Sponsors with fiscal-host support;
3. evaluate an Open Collective / fiscal-host path;
4. keep domestic support channels as owner-confirmed options, not public QR
   code dumps;
5. postpone Ko-fi / Buy Me a Coffee unless Stripe or PayPal payout can be
   verified for the maintainer.

## Matrix

| Channel | International fit | Mainland China fit | Overseas bank/card dependency | Current status | Recommendation |
| --- | --- | --- | --- | --- | --- |
| GitHub Sponsors | High | Uncertain | Needs supported-region payout or fiscal host | Not active | First formal channel to evaluate |
| GitHub Sponsors + fiscal host | High | Potentially better | Host may reduce direct banking burden | Not active | Best international-first candidate if available |
| Open Collective / fiscal host | High | Potentially better | Fiscal host may hold/manage funds | Not active | Strong candidate for transparent community funding |
| Ko-fi | High | Uncertain/low | Commonly depends on PayPal or Stripe | Not active | Postpone until payout path is verified |
| Buy Me a Coffee | High | Uncertain/low | Uses Stripe onboarding for payouts | Not active | Postpone until Stripe payout path is verified |
| Afdian or similar domestic platform | Low international fit | High domestic fit | Usually domestic-account oriented | Not active | Candidate for mainland supporters after owner review |
| Alipay / WeChat direct support | Low international fit | High domestic fit | Domestic-account oriented | Not active | Use cautiously; avoid exposing personal QR codes by default |
| Email-based sponsorship inquiry | Medium | Medium | None until a channel is chosen | Active as contact path | Safe current fallback |

## Channel notes

### GitHub Sponsors

GitHub Sponsors is the most natural fit for an open source repository because
it appears in the GitHub user and repository flow. However, GitHub requires
eligible account setup, payout information, tax information, and approval.

Official references:

- [Setting up GitHub Sponsors for your personal account](https://docs.github.com/en/sponsors/receiving-sponsorships-through-github-sponsors/setting-up-github-sponsors-for-your-personal-account)
- [Using a fiscal host to receive GitHub Sponsors payouts](https://docs.github.com/en/sponsors/receiving-sponsorships-through-github-sponsors/using-a-fiscal-host-to-receive-github-sponsors-payouts)
- [Displaying a sponsor button in your repository](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/displaying-a-sponsor-button-in-your-repository)

Important boundary:

- Do not list GitHub Sponsors as active until the owner has completed setup and
  the public sponsorship profile works while logged out.
- If choosing a fiscal host, evaluate that option during initial setup rather
  than assuming it can be switched later without support.

### Fiscal host / Open Collective

A fiscal host may help an unincorporated maintainer or project receive,
manage, and spend funds without first creating a legal entity or direct project
bank account. This can be valuable for a small public-good project, but it
also introduces host policy, fees, review, and governance responsibilities.

Official/reference entry:

- [Open Collective: What is fiscal hosting?](https://opencollective.com/fiscal-hosting)

Important boundary:

- A fiscal host is not just a payment button. It is a governance and trust
  relationship.
- Do not claim fiscal-host funding is active until a host has accepted the
  project and the public page is verified.

### Ko-fi

Ko-fi can be convenient for international supporters, but creator payout
support depends on payment-provider availability such as Stripe and/or PayPal.

Official reference:

- [Ko-fi: Can I use Stripe in my country?](https://help.ko-fi.com/hc/en-us/articles/360009265834-Can-I-use-Stripe-in-my-country)

Important boundary:

- Do not add Ko-fi until payout can be completed from the maintainer's real
  account context.

### Buy Me a Coffee

Buy Me a Coffee is simple for supporters, but creator payout setup currently
depends on Stripe onboarding.

Official reference:

- [Buy Me a Coffee: How do you set up payouts on your page?](https://help.buymeacoffee.com/en/articles/10025793-how-do-you-set-up-payouts-on-your-buy-me-a-coffee-page)

Important boundary:

- Do not add Buy Me a Coffee until Stripe payout onboarding works for the
  maintainer.

### Domestic support channels

Domestic platforms or direct domestic payments may be more practical for
mainland supporters. They should still be treated as public identity and
privacy surfaces, not casual personal contact dumps.

Possible options:

- Afdian or similar creator-support platforms;
- Alipay;
- WeChat Pay.

Important boundary:

- Avoid publishing personal QR codes by default.
- Prefer an owner-controlled public support page or a private-contact step
  until the maintainer intentionally accepts the public identity exposure.
- Keep tax, accounting, platform, and identity implications outside repository
  automation.

## Activation checklist

Before activating any direct funding link:

- [ ] owner confirms the account is intended for this project;
- [ ] public URL works while logged out;
- [ ] payout path is verified or the limitation is documented;
- [ ] personal contact, QR codes, and private identity surfaces are reviewed;
- [ ] fees and settlement limitations are understood;
- [ ] README and `docs/support-and-sponsorship.md` are updated;
- [ ] `.github/FUNDING.yml` is updated only with active, owner-controlled links;
- [ ] repository verification passes;
- [ ] no-pay-to-approve policy remains visible.

## No-pay-to-approve policy

Funding must not buy:

- resource inclusion;
- score/ranking boosts;
- curated Skill approval;
- bypass of license, provenance, safety, privacy, or review gates;
- access to private configuration, memory, private bookmarks, or private
  project internals.

Sponsorship can fund maintenance, review time, documentation, automation, and
public-safe examples. It cannot change the trust boundary.
