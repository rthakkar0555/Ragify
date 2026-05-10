/**
 * RAGify TypeScript SDK Client
 */

export interface RAGifyConfig {
  apiKey: string;
  baseUrl?: string;
}

export class RAGifyClient {
  private apiKey: string;
  private baseUrl: string;

  constructor(config: RAGifyConfig) {
    this.apiKey = config.apiKey;
    this.baseUrl = config.baseUrl || "https://api.ragify.dev/v1";
  }

  // TODO: Implement query, search, ingest, list methods
}
