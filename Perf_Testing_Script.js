import http from 'k6/http';
import { sleep, check } from 'k6';

export let options = {
stages: [
  { duration: '2m', target: 10 },
  { duration: '5m', target: 50 }, 
  { duration: '2m', target: 100 }, 
  { duration: '2m', target: 0 }, 
],
thresholds: {
http_req_duration: ['p(95)<500'], // 95% of requests under 500ms
http_req_failed: ['rate<0.1'], // Error rate under 10%
},
};

export default function() {
   let res1 = http.get('https://dummyjson.com/products');
  check(res1, { 'GET /products status is 200': (r) => r.status === 200 });

  let res2 = http.get('https://dummyjson.com/products/search?q=phone');
  check(res2, { 'Search phone status is 200': (r) => r.status === 200 });

  let res3 = http.get('https://dummyjson.com/products/1');
  check(res3, { 'Get product details status is 200': (r) => r.status === 200 });

  let res4 = http.post('https://dummyjson.com/carts/add', JSON.stringify({
    userId: 1,
    products: [{ id: 1, quantity: 1 }]
  }), {
    headers: { 'Content-Type': 'application/json' },
  });
  check(res4, { 'Add to cart status is 200': (r) => r.status === 200 });

  let res5 = http.get('https://dummyjson.com/carts/user/1');
  check(res5, { 'Checkout simulation status is 200': (r) => r.status === 200 });

  sleep(1);
}
