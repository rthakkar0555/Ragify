/**
 * SDK model types
 */

export interface RAGifyConfig {
  apiKey: string;
  baseUrl?: string;
}

export interface QueryOptions {
  collection?: string;
  topK?: number;
  rerank?: boolean;
  filters?: Record<string, unknown>;
}

export interface SearchResult {
  id: string;
  content: string;
  score: number;
  metadata: Record<string, unknown>;
}
