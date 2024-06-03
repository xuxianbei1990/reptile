# coding: utf-8
from sqlalchemy import Column, DECIMAL, DateTime, JSON, String, Text, text
from sqlalchemy.dialects.mysql import BIGINT, INTEGER, TINYINT, VARCHAR
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class OrderMain(Base):
    __tablename__ = 'order_main'
    __table_args__ = {'comment': '商品订单主表'}

    id = Column(BIGINT(20), primary_key=True, comment='订单id')
    order_no = Column(String(64, 'utf8mb4_unicode_ci'), nullable=False, comment='订单号')
    spu_id = Column(BIGINT(20), comment='spu_id')
    category_id = Column(BIGINT(20), comment='品类id,sales_category.id')
    goods_sku_id = Column(BIGINT(20), nullable=False, comment='goodskuId（商品定义）')
    order_sku_id = Column(BIGINT(20), comment='sku_id')
    order_sku_num = Column(INTEGER(11), nullable=False, comment='商品数量')
    user_id = Column(BIGINT(20), nullable=False, comment='下单用户id')
    leader_id = Column(BIGINT(20), nullable=False, comment='团长id')
    supplier_id = Column(BIGINT(20), nullable=False, comment='商家id')
    task_id = Column(BIGINT(20), comment='任务id')
    order_status = Column(TINYINT(2), nullable=False, comment='订单状态（0：待支付；1待发货；2待收货；3已完成签收；4已取消,5,超时自动签收）6：退货已完成, 7:超时取消;8:已退款;9:售后')
    after_status = Column(TINYINT(2), nullable=False, server_default=text("'0'"), comment='售后状态（0:初始状态；1： 已提交2：已撤销；3：团已处理-同意退货；4：团已处理-拒绝退货；5：商家已处理-同意退货；6：商家已处理-拒绝退货;')
    pay_status = Column(TINYINT(255), nullable=False, comment='支付状态（1 待付款；2 支付中；3 支付成功；4  已取消;；5支付失败, 6.超时取消,7:已退款）')
    mer_order_id = Column(String(64, 'utf8mb4_unicode_ci'), comment='交易编号')
    source_price = Column(DECIMAL(20, 0), nullable=False, comment='订单总金额（原价,  统一存分）')
    real_price = Column(DECIMAL(20, 0), nullable=False, comment='订单总金额（实际，统一存分）')
    supply_price = Column(DECIMAL(20, 0), nullable=False, comment='商品供货价（原价,  统一存分）')
    retail_price = Column(DECIMAL(20, 0), nullable=False, comment='商品零售价（原价,  统一存分）')
    leader_distribute = Column(DECIMAL(10, 0), comment='团长分红')
    supplier_distribute = Column(DECIMAL(10, 0), comment='商家分红')
    pay_time = Column(DateTime, comment='支付时间')
    spu_name = Column(String(64, 'utf8mb4_unicode_ci'), nullable=False, comment='商品名称')
    goods_id = Column(BIGINT(20), nullable=False, comment='商品goodis（商品定义）')
    sku_prop = Column(Text(collation='utf8mb4_unicode_ci'), nullable=False, comment='商品规格')
    sku_image = Column(String(1000, 'utf8mb4_unicode_ci'), nullable=False, comment='商品图片')
    deliver_time = Column(DateTime, comment='发货时间')
    deal_time = Column(DateTime, comment='成交时间')
    order_remark = Column(String(255, 'utf8mb4_unicode_ci'), comment='订单备注')
    user_name = Column(String(255, 'utf8mb4_unicode_ci'), comment='买家信息')
    leader_name = Column(String(255, 'utf8mb4_unicode_ci'), comment='团长名称')
    order_type = Column(TINYINT(2), comment='订单类型6:一件代发7：拼车；8：试样')
    create_time = Column(DateTime, server_default=text("CURRENT_TIMESTAMP"), comment='创建时间')
    creator_id = Column(BIGINT(20), comment='创建人')
    update_time = Column(DateTime, server_default=text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"), comment='修改时间')
    updator_id = Column(BIGINT(20), comment='修改人')
    delete_flag = Column(TINYINT(2), server_default=text("'0'"), comment='删除标志[ 0未删除  1已删除  默认0 ; 2用户删除]')
    remark = Column(String(255, 'utf8mb4_unicode_ci'), comment='备注')
    tag = Column(JSON, comment='标签json')
    batch_flag = Column(INTEGER(11), server_default=text("'0'"), comment='主订单跑批状态，默认为0，待处理；1，处理中，此时跑批但是未完成；2，跑批处理结束，完成分账确认；3，完成退款；4，放弃分账和到货')
    creator = Column(VARCHAR(50), comment='yudao')
    updater = Column(VARCHAR(50), comment='yudao')
    deleted = Column(INTEGER(11), server_default=text("'0'"), comment='yudao删除标志')
    tenant_id = Column(INTEGER(11), server_default=text("'1'"), comment='yudao多租户')
    article_number = Column(String(255, 'utf8mb4_unicode_ci'), server_default=text("''"), comment='货号')
    grounding_type = Column(TINYINT(2))

    # 订单字段打印
    def __str__(self):
        return str(vars(self))