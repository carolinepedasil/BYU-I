const swaggerJSDoc = require('swagger-jsdoc');

const RENDER_URL = process.env.RENDER_URL;

const options = {
  definition: {
    openapi: '3.0.0',
    info: {
      title: 'Product Inventory API',
      version: '1.0.0',
      description: 'API for managing products in an inventory system',
    },
    servers: [
      {
        url: RENDER_URL,
        description: 'Auto URL from .env or fallback to localhost',
      },
    ],
    components: {
      schemas: {
        Product: {
          type: 'object',
          required: ['name', 'price', 'stock', 'sku'],
          properties: {
            name: {
              type: 'string',
              example: 'Wireless Mouse'
            },
            description: {
              type: 'string',
              example: 'A reliable wireless mouse with USB receiver'
            },
            price: {
              type: 'number',
              example: 29.99
            },
            category: {
              type: 'string',
              example: 'Electronics'
            },
            stock: {
              type: 'number',
              example: 100
            },
            imageUrl: {
              type: 'string',
              example: 'http://example.com/images/mouse.png'
            },
            sku: {
              type: 'string',
              example: 'MOUSE123'
            }
          }
        },
        Category: {
          type: 'object',
          required: ['name'],
          properties: {
            name: {
              type: 'string',
              example: 'Electronics'
            },
            description: {
              type: 'string',
              example: 'Devices and gadgets'
            },
            createdAt: {
              type: 'string',
              format: 'date-time',
              example: '2025-09-10T12:34:56Z'
            }
          }
        },
        User: {
          type: 'object',
          required: ['username', 'password'],
          properties: {
            username: { type: 'string', example: 'admin' },
            password: { type: 'string', example: '123456' },
            createdAt: {
              type: 'string',
              format: 'date-time',
              example: '2025-09-27T21:53:35.669Z'
            },
            updatedAt: {
              type: 'string',
              format: 'date-time',
              example: '2025-09-27T21:53:35.669Z'
            }
          }
        },
      }
    },
    securitySchemes: {
      cookieAuth: {
        type: 'apiKey',
        in: 'cookie',
        name: 'connect.sid',
      },
    },
  },
  apis: ['./routes/*.js']
};

const swaggerSpec = swaggerJSDoc(options);

module.exports = swaggerSpec;