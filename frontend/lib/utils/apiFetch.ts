// export async function apiFetch<T>(
//   url: string,
//   fetchParams: RequestInit,
// ): Promise<T> {
// //   const accessToken = await getAccessToken();
//   const fetchOptions: RequestInit = {
//     method: fetchParams?.method || "GET",
//     headers: {
//       Authorization: `Bearer ${accessToken}`,
//       "Content-Type": "application/json",
//       ...fetchParams?.headers,
//     },
//     body: fetchParams?.body,
//   };
// }
