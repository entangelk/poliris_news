## Polaris sharetech Road to BlockChain AI

## 개요

```
최근 폴라리스 오피스의 주식가격과 폴라리스 쉐어토큰의 상관관계를 알아보고
해당 내용의 뉴스 토픽 분석을 진행한다.

아울러 시계열 머신러닝을 통해 앞으로의 토큰 가격을 예상해보고 미래 전략에 대해 알아본다.
```

## 결론

[최종 보고서](https://docs.google.com/presentation/d/1q89uSEslWp1AvbcVDwEit3KO1EywVichYd2ALYba3K0/edit#slide=id.p)

### 시계열 예측 모델

- 사용 모델 : facebook.prophet

- LDA 분석에서 나온 결론으로 AI와 관련된 블록체인 사업전략을 영위하였을 시 토큰 가격은 우상향 할 것이다.

![시계열 예측](./docs/image/forecase_fig_ai.png)

![시계열 분석](./docs/image/components_ai.png)

```
부가적 분석으로 토큰은 주중보다는 주말 부근에서 더 긍정적인 거래가 많이 일어났고, 
지난 2023년 동안 4월에 매우 많이 올랐다가 6월에 최저치를 찍었다.
그리고 다시 그 이후부터 다시 우상향 하는 중이다.
```


## 토픽 추출 모델

```
- 사용 모델 : sklearn.LatentDirichletAllocation
- 평가 모델 : gensim.coherencemodel
- Tokenizer : Okt
- Vectorizer : sklearn.TfidfVectorizer
```

## 세부 분석

![주가-토큰](./docs/image/stock_token.png)

```
지난 2021년 이후 폴라리스오피스 주가와 폴라쉐어토큰의 가격을 비교한 그래프이다.
상호 가격변동의 기간이 동일하다는 것을 알 수 있다.

토큰이 강세였던 2021년에는 주가가 폴라토큰의 영향을, 토큰이 약세였던 2022년 이후에는 폴라토큰이 주가의 영향을 받고 있어 서로 상호 보완적 관계라는 것을 알 수있다.
```

![주가예측](./docs/image/predict_stock_token.png)
```
현 테마를 정상적으로 유지한다면

주가
예측 모델에 의한 차후 반년간 주가 평균 가격 상승 약 75%
시가총액 약 2500억원 상승 효과

토큰
예측 모델에 의한 차후 반년간 토큰 평균 가격 상승 약 30%
시가총액 약 60억원 상승 효과
```

## 기타 분석

![주가현황](./docs/image/stock_fig.png)

```
12월과 1월 / 3월과 4월 사이에 평균적으로 다른 달들보다 부정적인 내용이 많았음
```

